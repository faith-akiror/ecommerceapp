from fastapi import FastAPI
from contextlib import asynccontextmanager

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
    print("Application startup: Creating database tables...")
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown event
    print("Application shutdown: Database connection pool closed (if applicable).")
    # In a real application, you might want to explicitly close engine if it's not handled by SQLAlchemy's default behavior

app = FastAPI(
    title="Ecommerce API",
    version="1.0.0",
    lifespan=lifespan # Use the new lifespan context manager
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