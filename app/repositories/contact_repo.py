from sqlalchemy.orm import Session
from app.models.contact import Contact


class ContactRepository:

    def save(self, db: Session, contact: Contact):
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return contact

    def find_all(self, db: Session):
        return db.query(Contact).all()
