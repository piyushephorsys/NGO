import base64
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
        number: str,
        email: str,
        pan_number: str,
        address: str,
        file: UploadFile
    ):
        file_bytes = file.file.read()

        document = Donate(
            name=name,
            number=number,
            email=email,
            pan_number=pan_number,
            address=address,
            file_name=file.filename,
            file_type=file.content_type,
            file_data=file_bytes
        )

        saved_doc = self.repo.save(db, document)

        return {
            "id": saved_doc.id,
            "name": saved_doc.name,
            "number": saved_doc.number,
            "email": saved_doc.email,
            "pan_number": saved_doc.pan_number,
            "address": saved_doc.address,
            "file_name": saved_doc.file_name,
            "file_type": saved_doc.file_type,
            "image_url": f"/donate/{saved_doc.id}/image"
        }
    
    def get_all_documents(self, db: Session):
        docs = self.repo.find_all(db)
        return [
            {
                "id": doc.id,
                "name": doc.name,
                "number": doc.number,
                "email": doc.email,
                "pan_number": doc.pan_number,
                "address": doc.address,
                "file_name": doc.file_name,
                "file_type": doc.file_type,
                "image_url": f"/donate/{doc.id}/image"
            }
            for doc in docs
        ]

    # def get_all_documents(self, db: Session):
    #     documents = self.repo.find_all(db)
    #     return [self._map_to_response(doc) for doc in documents]

    def get_file_by_id(self, db: Session, doc_id: int):
        document = self.repo.find_by_id(db, doc_id)
        if not document:
            return None
        return self._map_to_response(document)

    # def _map_to_response(self, document: Donate):
    #     file_base64 = None
    #     if document.file_data:
    #         file_base64 = base64.b64encode(document.file_data).decode("utf-8")

    #     return {
    #         "id": document.id,
    #         "name": document.name,
    #         "number": document.number,
    #         "email": document.email,
    #         "pan_number": document.pan_number,
    #         "address": document.address,
    #         "file_name": document.file_name,
    #         "file_type": document.file_type,
    #         "file_base64": file_base64
    #     }
