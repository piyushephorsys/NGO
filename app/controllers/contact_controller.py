from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.contact import ContactCreate, ContactResponse
from app.services.contact_service import ContactService

contactRouter = APIRouter(prefix="/contacts", tags=["Contacts"])
service = ContactService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@contactRouter.post("/", response_model=ContactResponse)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return service.create_contact(db, contact)

@contactRouter.get("/", response_model=list[ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    return service.get_all_contacts(db)
