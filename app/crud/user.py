from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password
from app.crud.base import CRUD


class CRUDUser(CRUD):
    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, data: dict):
        data["password"] = hash_password(data["password"])
        return super().create(db, data)


user_crud = CRUDUser(User)