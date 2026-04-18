from fastapi import FastAPI
from contextlib import asynccontextmanager
import time
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from app.db.base import Base
from app.db.session import engine
from app.api.v1.routes import (
    auth,
    users,
    products,
    cart,
    orders,
    delivery
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    print("Application startup: Waiting for database connection...")
    max_retries = 30
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Test database connection
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
                print("Database connection successful!")

            # Create tables
            print("Creating database tables...")
            Base.metadata.create_all(bind=engine)
            print("Database tables created successfully!")
            break
        except OperationalError as e:
            retry_count += 1
            print(f"Database connection failed (attempt {retry_count}/{max_retries}): {e}")
            if retry_count < max_retries:
                print("Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("Max retries reached. Application will start without database tables.")
                break
        except Exception as e:
            print(f"Unexpected error during database setup: {e}")
            break

    yield
    # Shutdown event
    print("Application shutdown: Database connection pool closed (if applicable).")


app = FastAPI(
    title="Ecommerce API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(cart.router, prefix="/api/v1/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["Orders"])
app.include_router(delivery.router, prefix="/api/v1/delivery", tags=["Delivery"])


@app.get("/health")
def health():
    return {"status": "ok"}