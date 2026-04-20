import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import type { Product } from '../services/productService';
import { productService } from '../services/productService';
import '../styles/pages.css';

export default function HomePage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const data = await productService.getAll(0, 8);
        setProducts(data);
      } catch (err) {
        setError('Failed to load products');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) return <div className="container"><p>Loading products...</p></div>;
  if (error) return <div className="container error"><p>{error}</p></div>;

  return (
    <div className="container">
      <div className="hero">
        <h1>Welcome to Ecommerce</h1>
        <p>Discover amazing products at great prices</p>
      </div>

      <div className="products-grid">
        {products.map((product) => (
          <Link key={product.id} to={`/product/${product.id}`} className="product-card">
            <div className="product-image">
              <img src={product.image_url || 'https://via.placeholder.com/250'} alt={product.name} />
            </div>
            <h3>{product.name}</h3>
            <p className="price">${product.price.toFixed(2)}</p>
            <p className="stock">{product.stock > 0 ? 'In Stock' : 'Out of Stock'}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
