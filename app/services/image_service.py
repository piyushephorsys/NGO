from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.repositories.image_repo import ImageRepository
from app.models.image import Image

class ImageService:

    def __init__(self):
        self.repo = ImageRepository()

    def add_image(
        self,
        db: Session,
        file: UploadFile,
        description: str,
        heading: str
    ):
        image_bytes = file.file.read()

        image = Image(
            filename=file.filename,
            content_type=file.content_type,
            description=description,
            image_data=image_bytes,
            heading=heading
        )

        return self.repo.save(db, image)


    def get_all_images(self, db: Session):
        return self.repo.get_all(db)

    def get_image(self, db: Session, image_id: int):
        return self.repo.get_by_id(db, image_id)
