import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ProductPage from './pages/ProductPage';
import CartPage from './pages/CartPage';
import './App.css';

function App() {
  return (
    <Router>
      <header className="header">
        <nav className="navbar">
          <Link to="/" className="navbar-brand">Ecommerce</Link>
          <div className="navbar-links">
            <Link to="/">Home</Link>
            <Link to="/cart" className="cart-link">
              🛒 Cart
            </Link>
          </div>
        </nav>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/product/:id" element={<ProductPage />} />
          <Route path="/cart" element={<CartPage />} />
        </Routes>
      </main>

      <footer className="footer">
        <p>&copy; 2024 Ecommerce App. All rights reserved.</p>
      </footer>
    </Router>
  );
}

export default App;
