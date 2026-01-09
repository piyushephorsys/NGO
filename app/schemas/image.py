from pydantic import BaseModel

class ImageResponse(BaseModel):
    id: int
    filename: str
    description: str
    heading: str

    class Config:
        from_attributes = True
