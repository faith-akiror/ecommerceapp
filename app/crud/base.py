class CRUD:
    def __init__(self, model):
        self.model = model

    def create(self, db, data: dict):
        obj = self.model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get(self, db, id: int):
        return db.query(self.model).filter_by(id=id).first()

    def get_all(self, db, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(self, db, obj, data: dict):
        for key, value in data.items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db, obj):
        db.delete(obj)
        db.commit()
        return obj