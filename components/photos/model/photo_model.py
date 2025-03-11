from sqlalchemy import Column, Integer, String
from database import Base

class Photo(Base):
    __tablename__ = "photos"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)