import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import type { Product } from '../services/productService';
import { productService } from '../services/productService';
import { cartService } from '../services/cartService';
import '../styles/pages.css';

export default function ProductPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [product, setProduct] = useState<Product | null>(null);
  const [quantity, setQuantity] = useState(1);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [adding, setAdding] = useState(false);

  useEffect(() => {
    if (!id) return;

    const fetchProduct = async () => {
      try {
        const data = await productService.getById(parseInt(id));
        setProduct(data);
      } catch (err) {
        setError('Failed to load product');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  const handleAddToCart = async () => {
    if (!product || quantity < 1) return;

    setAdding(true);
    try {
      await cartService.addItem(product.id, quantity);
      alert('Added to cart!');
      navigate('/cart');
    } catch (err) {
      alert('Failed to add to cart');
      console.error(err);
    } finally {
      setAdding(false);
    }
  };

  if (loading) return <div className="container"><p>Loading product...</p></div>;
  if (error) return <div className="container error"><p>{error}</p></div>;
  if (!product) return <div className="container error"><p>Product not found</p></div>;

  return (
    <div className="container">
      <button onClick={() => navigate(-1)} className="back-button">← Back</button>
      <div className="product-detail">
        <div className="product-image-large">
          <img src={product.image_url || 'https://via.placeholder.com/500'} alt={product.name} />
        </div>
        <div className="product-info">
          <h1>{product.name}</h1>
          <p className="description">{product.description}</p>
          <p className="price-large">${product.price.toFixed(2)}</p>
          <p className={product.stock > 0 ? 'in-stock' : 'out-of-stock'}>
            {product.stock > 0 ? `${product.stock} in stock` : 'Out of stock'}
          </p>
          
          {product.stock > 0 && (
            <div className="add-to-cart">
              <div className="quantity-control">
                <button onClick={() => setQuantity(Math.max(1, quantity - 1))}>-</button>
                <input 
                  type="number" 
                  min="1" 
                  max={product.stock}
                  value={quantity}
                  onChange={(e) => setQuantity(Math.max(1, parseInt(e.target.value) || 1))}
                />
                <button onClick={() => setQuantity(Math.min(product.stock, quantity + 1))}>+</button>
              </div>
              <button 
                onClick={handleAddToCart} 
                disabled={adding}
                className="btn-primary"
              >
                {adding ? 'Adding...' : 'Add to Cart'}
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
