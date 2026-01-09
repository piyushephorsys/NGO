from sqlalchemy.orm import Session
from app.models.onlyImage import Image

class ImageRepository:

    def save(self, db: Session, image: Image):
        db.add(image)
        db.commit()
        db.refresh(image)
        return image

    def find_all(self, db: Session):
        return db.query(Image).all()

    def find_by_id(self, db: Session, image_id: int):
        return db.query(Image).filter(Image.id == image_id).first()
