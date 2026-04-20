# Ecommerce Frontend

A React + TypeScript frontend for the ecommerce application built with Vite.

## Features

- **Product Browsing**: View products from the backend API
- **Product Details**: View detailed information about each product
- **Shopping Cart**: Add products to cart and manage quantities
- **API Integration**: Axios-based API client with automatic token handling
- **Responsive Design**: Mobile-friendly UI
- **Routing**: React Router for navigation

## Getting Started

### Prerequisites

- Node.js 18+ and npm

### Installation

```bash
cd frontend
npm install
```

### Development

```bash
npm run dev
```

The app will start at `http://localhost:5173` and proxy API calls to `http://localhost:8000/api/v1`.

### Build

```bash
npm run build
```

### Lint

```bash
npm run lint
```

## Project Structure

```
src/
├── pages/           # Page components
├── services/        # API service clients
├── styles/          # CSS stylesheets
├── App.tsx          # Main app with routing
└── main.tsx         # Entry point
```

## Services

### API Client (`services/api.ts`)
- Axios instance configured for the API
- Auto token injection in headers
- 401 redirect to login on auth failure

### Product Service (`services/productService.ts`)
- `getAll()`: Fetch all products with pagination
- `getById()`: Fetch product by ID
- `search()`: Search products by query

### Auth Service (`services/authService.ts`)
- `login()`: Login user
- `register()`: Register new user
- `logout()`: Logout user
- `getCurrentUser()`: Get logged-in user
- `isAuthenticated()`: Check auth status

### Cart Service (`services/cartService.ts`)
- `getCart()`: Fetch user's cart
- `addItem()`: Add product to cart
- `updateItem()`: Update item quantity
- `removeItem()`: Remove item from cart
- `clearCart()`: Clear entire cart

## Environment Variables

Create a `.env` file in the frontend directory:

```
VITE_API_URL=http://localhost:8000/api/v1
```

## Development Notes

- The app proxies API calls through Vite's dev server to avoid CORS issues
- Authentication tokens are stored in localStorage
- Components use hooks for state management
