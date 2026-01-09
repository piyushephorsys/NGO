from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.onlyImage import OnlyImageService
from app.schemas.onlyImage import ImageResponse

OnlyImagerouter = APIRouter(prefix="/onlyImage", tags=["OnlyImages"])
service = OnlyImageService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@OnlyImagerouter.post("/upload")
def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    image = service.upload_image(db, file)
    return {
        "id": image.id,
        "message": "Image uploaded successfully"
    }


@OnlyImagerouter.get("/", response_model=list[ImageResponse])
def get_all_images(db: Session = Depends(get_db)):
    images = service.get_all_images(db)
    return [
        ImageResponse(
            id=img.id,
            filename=img.filename,
            image_url=f"/images/{img.id}"
        )
        for img in images
    ]


@OnlyImagerouter.get("/{image_id}")
def get_image(image_id: int, db: Session = Depends(get_db)):
    image = service.get_image_by_id(db, image_id)

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=image.image_data,
        media_type=image.content_type
    )
