from pydantic import BaseModel

class ImageResponse(BaseModel):
    id: int
    filename: str
    image_url: str

    class Config:
        from_attributes = True
