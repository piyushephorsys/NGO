from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.models.onlyImage import Image
from app.repositories.onlyImage import ImageRepository

class OnlyImageService:

    def __init__(self):
        self.repo = ImageRepository()

    def upload_image(self, db: Session, file: UploadFile):
        image = Image(
            filename=file.filename,
            content_type=file.content_type,
            image_data=file.file.read()
        )
        return self.repo.save(db, image)

    def get_all_images(self, db: Session):
        return self.repo.find_all(db)

    def get_image_by_id(self, db: Session, image_id: int):
        return self.repo.find_by_id(db, image_id)
