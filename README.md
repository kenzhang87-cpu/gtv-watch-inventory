# GTV - Watch Inventory & P&L Tracker

A comprehensive single-page web application for tracking watch inventory, purchases, sales, and profit/loss calculations.

![GTV Screenshot](https://kenzhang.tech/gtv/)

## Features

### 📊 Dashboard & Statistics
- **Watches In Stock**: Current inventory count
- **Watches Sold**: Total sold items
- **Inventory Value**: Total value of current stock
- **Total Profit**: Cumulative profit from all sales
- **Total Investment**: Sum of all purchase costs
- **Total Revenue**: Sum of all sales

### 📈 Charts & Visualizations
- **Profit Over Time**: Line chart showing profit trends by month
- **Inventory by Brand**: Doughnut chart of stock distribution
- **Sales Trend**: Bar chart of watches sold per month
- **Profit by Brand**: Bar chart comparing profitability across brands

### ⌚ Inventory Management
- Add, edit, and delete watch entries
- Track key details:
  - SKU (unique identifier)
  - Brand & Model
  - Purchase date & price
  - Sale date & price (when applicable)
  - Additional costs (shipping, service, authentication, etc.)
  - Status (In Stock, Sold, Pending)
  - Notes

### 💰 Profit Calculation
- Automatic profit calculation: `Sale Price - Purchase Price - Additional Costs`
- Color-coded profit display (green for positive, red for negative)
- Individual profit tracking per SKU

### 📝 Data Persistence
- **LocalStorage**: Data automatically saves to browser storage
- **Export**: Download inventory as JSON file
- **Import**: Restore from previously exported JSON file

### ✏️ Inline Editing
- Click any field in the table to edit directly
- Real-time updates to calculations and charts

### 🔍 Filtering & Search
- Search by SKU, brand, or model
- Filter by status (In Stock, Sold, Pending)
- Filter by brand

## Deployment

**Live URL**: https://kenzhang.tech/gtv/

The application is a static HTML file that can be deployed to any web server.

## Sample Data

The app comes pre-loaded with sample data to demonstrate functionality:
- Rolex Submariner (Sold)
- Omega Speedmaster (In Stock)
- Patek Philippe Nautilus (Sold)
- Audemars Piguet Royal Oak (In Stock)
- Rolex GMT-Master II (Pending)

## Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS variables
- **Vanilla JavaScript** - No framework dependencies
- **Chart.js** - Data visualization
- **LocalStorage API** - Client-side data persistence

## Usage

1. Open the application in a web browser
2. Use the "+ Add Watch" button to add new inventory items
3. Click table cells to edit data inline
4. Use Export/Import buttons to backup or restore data
5. Monitor statistics and charts for business insights

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

MIT License - Feel free to use and modify as needed.

---

Built with ❤️ for GTV Watch Business
