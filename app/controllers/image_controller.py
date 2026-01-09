from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.image_service import ImageService
from app.schemas.image import ImageResponse

Image_router = APIRouter(prefix="/images", tags=["Images"])
service = ImageService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@Image_router.post("/")
def upload_image(
    description: str = Form(...),
    heading: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    image = service.add_image(db, file, description, heading)

    return {    
        "id": image.id,
        "filename": image.filename,
        "description": image.description,
        "heading": image.heading,
        "message": "Image uploaded successfully"
    }


@Image_router.get("/", response_model=list[ImageResponse])
def get_all_images(db: Session = Depends(get_db)):
    return service.get_all_images(db)


@Image_router.get("/{image_id}")
def get_image(image_id: int, db: Session = Depends(get_db)):
    image = service.get_image(db, image_id)

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=image.image_data,
        media_type=image.content_type
    )


