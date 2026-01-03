from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from datetime import datetime
from app.database import Base

class Donate(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(String)
    email = Column(String)
    pan_number = Column(String)
    address = Column(String)

    file_name = Column(String)
    file_type = Column(String)
    file_data = Column(LargeBinary)

    created_at = Column(DateTime, default=datetime.now)
