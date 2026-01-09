from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.models.donate import Donate
from app.repositories.donate_repo import DonateRepository

class DonateService:

    def __init__(self):
        self.repo = DonateRepository()

    def create_document(
        self,
        db: Session,
        name: str,
        phone: str,
        utr: str,
        pan: str,
        message: str,
        screenshot: UploadFile
    ):
        screenshot.file.seek(0)          # ✅ REQUIRED
        file_bytes = screenshot.file.read()

        document = Donate(
            name=name,
            phone=phone,
            utr=utr,
            screenshot=file_bytes,
            pan=pan,
            message=message
        )

        saved_doc = self.repo.save(db, document)

        return {
            "id": saved_doc.id,
            "name": saved_doc.name,
            "phone": saved_doc.phone,
            "utr": saved_doc.utr,
            "pan": saved_doc.pan,
            "message": saved_doc.message,
            "image_url": f"/donate/{saved_doc.id}/image"
        }

    def get_all_documents(self, db: Session):
        docs = self.repo.find_all(db)
        return [
            {
                "id": doc.id,
                "name": doc.name,
                "phone": doc.phone,
                "utr": doc.utr,
                "image_url": f"/donate/{doc.id}/image",
                "pan": doc.pan,
                "message": doc.message
            }
            for doc in docs
        ]
