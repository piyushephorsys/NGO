from pydantic import BaseModel

class ContactCreate(BaseModel):
    name: str
    phone: str
    email: str
    message: str
   

class ContactResponse(ContactCreate):
    id: int

    class Config:
        from_attributes = True
