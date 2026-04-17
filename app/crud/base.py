class CRUDBase:
    def __init__(self, model):
        self.model = model

    def get(self, db, id):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db):
        return db.query(self.model).all()

    def create(self, db, obj):
        db_obj = self.model(**obj.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db, db_obj, obj):
        for k, v in obj.dict().items():
            setattr(db_obj, k, v)
        db.commit()
        return db_obj

    def delete(self, db, db_obj):
        db.delete(db_obj)
        db.commit()