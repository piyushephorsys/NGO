from sqlalchemy.orm import Session
from app.models.donate import Donate

class DonateRepository:

    def save(self, db: Session, document: Donate):
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def find_all(self, db: Session):
        return db.query(Donate).all()

    def find_by_id(self, db: Session, doc_id: int):
        return db.query(Donate).filter(Donate.id == doc_id).first()
