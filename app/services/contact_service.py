from app.repositories.contact_repo import ContactRepository
from app.models.contact import Contact

class ContactService:

    def __init__(self):
        self.repo = ContactRepository()

    def create_contact(self, db, data):
        contact = Contact(**data.dict())
        return self.repo.save(db, contact)

    def get_all_contacts(self, db):
        return self.repo.find_all(db)
