from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.donate_service import DonateService

router = APIRouter(prefix="/donate", tags=["Donates"])
service = DonateService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def donate(
    name: str = Form(...),
    number: str = Form(...),
    email: str = Form(...),
    pan_number: str = Form(...),
    address: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return service.create_document(
        db, name, number, email, pan_number, address, file
    )

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all_documents(db)

@router.get("/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):

    return service.get_file_by_id(db, id)

from fastapi.responses import Response

@router.get("/{id}/image")
def get_donation_image(id: int, db: Session = Depends(get_db)):
    doc = service.repo.find_by_id(db, id)
    if not doc or not doc.file_data:
        return {"message": "Image not found"}

    return Response(
        content=doc.file_data,
        media_type=doc.file_type
    )

