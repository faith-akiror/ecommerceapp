from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here so Base.metadata.create_all and Alembic sees them
from app.models import user, product, cart, cart_item, order, delivery