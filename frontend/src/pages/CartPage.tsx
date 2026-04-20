import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import type { Cart } from '../services/cartService';
import { cartService } from '../services/cartService';
import '../styles/pages.css';

export default function CartPage() {
  const navigate = useNavigate();
  const [cart, setCart] = useState<Cart | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    try {
      const data = await cartService.getCart();
      setCart(data);
    } catch (err) {
      setError('Failed to load cart');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateQuantity = async (itemId: number, quantity: number) => {
    if (quantity < 1) {
      handleRemoveItem(itemId);
      return;
    }

    try {
      const updatedCart = await cartService.updateItem(itemId, quantity);
      setCart(updatedCart);
    } catch (err) {
      alert('Failed to update item');
      console.error(err);
    }
  };

  const handleRemoveItem = async (itemId: number) => {
    try {
      const updatedCart = await cartService.removeItem(itemId);
      setCart(updatedCart);
    } catch (err) {
      alert('Failed to remove item');
      console.error(err);
    }
  };

  const handleCheckout = () => {
    navigate('/checkout');
  };

  if (loading) return <div className="container"><p>Loading cart...</p></div>;
  if (error) return <div className="container error"><p>{error}</p></div>;

  if (!cart || cart.items.length === 0) {
    return (
      <div className="container">
        <h1>Shopping Cart</h1>
        <p className="empty-cart">Your cart is empty</p>
        <button onClick={() => navigate('/')} className="btn-primary">
          Continue Shopping
        </button>
      </div>
    );
  }

  return (
    <div className="container">
      <h1>Shopping Cart</h1>
      <div className="cart-items">
        {cart.items.map((item) => (
          <div key={item.id} className="cart-item">
            <div className="item-details">
              <h3>Product #{item.product_id}</h3>
              <p>Price: ${item.price.toFixed(2)}</p>
            </div>
            <div className="quantity-control">
              <button onClick={() => handleUpdateQuantity(item.id, item.quantity - 1)}>-</button>
              <span>{item.quantity}</span>
              <button onClick={() => handleUpdateQuantity(item.id, item.quantity + 1)}>+</button>
            </div>
            <p className="item-total">${(item.price * item.quantity).toFixed(2)}</p>
            <button 
              onClick={() => handleRemoveItem(item.id)} 
              className="btn-danger"
            >
              Remove
            </button>
          </div>
        ))}
      </div>
      <div className="cart-summary">
        <h2>Total: ${cart.total_price.toFixed(2)}</h2>
        <div className="cart-actions">
          <button onClick={() => navigate('/')} className="btn-secondary">
            Continue Shopping
          </button>
          <button onClick={handleCheckout} className="btn-primary">
            Proceed to Checkout
          </button>
        </div>
      </div>
    </div>
  );
}
