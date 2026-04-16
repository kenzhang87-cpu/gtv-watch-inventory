#!/usr/bin/env python3
import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

VIEWS_FILE = "/var/www/kenzhang.tech/gtv/views/views.json"
CORRECT_PASSWORD = "Lenny365"
VIEWS_DIR = os.path.dirname(VIEWS_FILE)

os.makedirs(VIEWS_DIR, exist_ok=True)

class APIHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Password')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def check_auth(self):
        password = self.headers.get('X-Password', '')
        return password == CORRECT_PASSWORD
    
    def load_views(self):
        if not os.path.exists(VIEWS_FILE):
            return []
        try:
            with open(VIEWS_FILE, 'r') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except:
            return []
    
    def save_views(self, views):
        with open(VIEWS_FILE, 'w') as f:
            json.dump(views, f, indent=2)
    
    def do_OPTIONS(self):
        self.send_json({'success': True})
    
    def do_GET(self):
        if not self.check_auth():
            self.send_json({'error': 'Unauthorized'}, 401)
            return
        views = self.load_views()
        view_list = [{
            'id': v['id'],
            'name': v['name'],
            'timestamp': v['timestamp'],
            'watchCount': len(v.get('watches', []))
        } for v in views]
        self.send_json({'success': True, 'views': view_list})
    
    def do_POST(self):
        if not self.check_auth():
            self.send_json({'error': 'Unauthorized'}, 401)
            return
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()
        try:
            data = json.loads(body)
        except:
            self.send_json({'error': 'Invalid JSON'}, 400)
            return
        action = data.get('action')
        views = self.load_views()
        if action == 'save':
            view = data.get('view', {})
            if not view.get('name'):
                self.send_json({'error': 'View name required'}, 400)
                return
            new_view = {
                'id': view.get('id', int(os.times()[0] * 1000)),
                'name': view['name'],
                'timestamp': view.get('timestamp', ''),
                'watches': view.get('watches', [])
            }
            views.append(new_view)
            self.save_views(views)
            self.send_json({
                'success': True,
                'view': {
                    'id': new_view['id'],
                    'name': new_view['name'],
                    'timestamp': new_view['timestamp'],
                    'watchCount': len(new_view['watches'])
                }
            })
        elif action == 'load':
            view_id = data.get('id')
            for view in views:
                if view['id'] == view_id:
                    self.send_json({'success': True, 'view': view})
                    return
            self.send_json({'error': 'View not found'}, 404)
        else:
            self.send_json({'error': 'Unknown action'}, 400)
    
    def do_DELETE(self):
        if not self.check_auth():
            self.send_json({'error': 'Unauthorized'}, 401)
            return
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()
        try:
            data = json.loads(body)
        except:
            self.send_json({'error': 'Invalid JSON'}, 400)
            return
        view_id = data.get('id')
        views = self.load_views()
        initial_count = len(views)
        views = [v for v in views if v['id'] != view_id]
        if len(views) < initial_count:
            self.save_views(views)
            self.send_json({'success': True})
        else:
            self.send_json({'error': 'View not found'}, 404)

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8081), APIHandler)
    server.serve_forever()
