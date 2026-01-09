from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.donate_service import DonateService
from fastapi.responses import Response

router = APIRouter(prefix="/donate", tags=["Donate"])
service = DonateService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_donation(
    name: str = Form(...),
    phone: str = Form(...),
    utr: str = Form(...),
     pan: str | None = Form(None),
    message: str = Form(...),
    screenshot: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return service.create_document(db, name, phone, utr, pan, message,screenshot)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all_documents(db)


@router.get("/{id}/image")
def get_donation_image(id: int, db: Session = Depends(get_db)):
    document = service.repo.find_by_id(db, id)
    if not document or not document.screenshot:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=document.screenshot,
        media_type="image/png"  # or image/jpeg if needed
    )
