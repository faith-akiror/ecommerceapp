# Ecommerce App

A full-stack ecommerce application with a FastAPI backend and React TypeScript frontend.

## Project Structure

```
ecommerceapp/
├── app/                      # FastAPI backend
│   ├── api/v1/               # API routes
│   ├── core/                 # Configuration and dependencies
│   ├── crud/                 # Database CRUD operations
│   ├── db/                   # Database setup
│   ├── models/               # SQLAlchemy models
│   ├── schemas/              # Pydantic schemas
│   └── main.py               # FastAPI app entry
├── frontend/                 # React TypeScript frontend
│   ├── src/
│   │   ├── pages/            # Page components
│   │   ├── services/         # API clients
│   │   ├── styles/           # CSS files
│   │   ├── App.tsx           # Main app with routing
│   │   └── main.tsx          # Entry point
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml        # Docker services configuration
├── Dockerfile                # Backend Docker image
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
docker-compose up
```

This will start:
- PostgreSQL database on port 5432
- FastAPI backend on port 8000 (`http://localhost:8000`)
- React frontend on port 5173 (`http://localhost:5173`)

### Option 2: Local Development

#### Backend Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the backend
uvicorn app.main:app --reload
```

Backend API: `http://localhost:8000`  
API Docs: `http://localhost:8000/docs`

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend: `http://localhost:5173`

## API Endpoints

### Products
- `GET /api/v1/products` - List all products
- `GET /api/v1/products/{id}` - Get product details
- `GET /api/v1/products/search?q=query` - Search products

### Cart
- `GET /api/v1/cart` - Get user's cart
- `POST /api/v1/cart/items` - Add item to cart
- `PUT /api/v1/cart/items/{id}` - Update cart item
- `DELETE /api/v1/cart/items/{id}` - Remove item from cart
- `DELETE /api/v1/cart` - Clear cart

### Authentication
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/auth/register` - Register new user

### Orders
- `GET /api/v1/orders` - List user's orders
- `POST /api/v1/orders` - Create new order
- `GET /api/v1/orders/{id}` - Get order details

### Delivery
- `GET /api/v1/delivery/{order_id}` - Get delivery status
- `PUT /api/v1/delivery/{order_id}` - Update delivery status

### Users
- `GET /api/v1/users/me` - Get current user
- `PUT /api/v1/users/me` - Update current user

## Frontend Features

- **Product Browsing**: View all products with pagination
- **Product Details**: Detailed view with images and description
- **Shopping Cart**: Add/remove items, manage quantities
- **Responsive Design**: Works on desktop and mobile
- **API Integration**: Axios client with auto token management

## Environment Setup

### Backend (.env)
Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ecommerce
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
REDIS_URL=redis://redis:6379/0
```

### Frontend (.env in frontend/)
Create a `.env` file in the frontend directory:

```env
VITE_API_URL=http://localhost:8000/api/v1
```

## Development

### Testing

```bash
# Test import of main app
python test_import.py
```

### Building

**Backend**:
```bash
docker build -t ecommerce-backend .
```

**Frontend**:
```bash
cd frontend
npm run build
```

### Linting

**Frontend**:
```bash
cd frontend
npm run lint
```

## Technologies Used

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **Server**: Gunicorn + Uvicorn
- **Task Queue**: Celery (optional)
- **Cache**: Redis (optional)

### Frontend
- **Framework**: React 18
- **Language**: TypeScript
- **Build Tool**: Vite
- **Routing**: React Router
- **HTTP Client**: Axios
- **Styling**: CSS

## Project Status

✅ Backend API fully implemented  
✅ Frontend React app scaffolded with routing  
✅ API integration ready  
⏳ Authentication UI pending  
⏳ Checkout flow pending  
⏳ Order management pending  

## Contributing

1. Create a feature branch
2. Make your changes
3. Test locally
4. Submit a pull request

## License

MIT License - feel free to use this project
