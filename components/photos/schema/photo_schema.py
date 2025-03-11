from pydantic import BaseModel

class PhotoSchema(BaseModel):
    id: int
    filename: str
    filepath: str
    
    class Config:
        from_attributes = True
