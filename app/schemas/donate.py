from pydantic import BaseModel
from typing import Optional


class DonateSchema(BaseModel):
    id: int
    name: str
    number: str
    email: str
    pan_number: str
    address: str

    file_name: Optional[str]
    file_type: Optional[str]
    file_base64: Optional[str]

    class Config:
        from_attributes  = True
