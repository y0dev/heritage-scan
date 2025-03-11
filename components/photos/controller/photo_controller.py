from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from pathlib import Path
import shutil

from database import get_db
from components.photos.schema.photo_schema import PhotoSchema
from components.photos.model.photo_model import Photo

router = APIRouter()

# Define the directory to store uploaded images
UPLOAD_DIR = Path("public/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload", response_model=PhotoSchema)
def upload_photo(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Uploads an image and saves metadata to the database.
    """
    try:
        file_location = UPLOAD_DIR / file.filename
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Save to database
        new_photo = Photo(filename=file.filename, filepath=str(file_location))
        db.add(new_photo)
        db.commit()
        db.refresh(new_photo)

        return new_photo
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

@router.get("/list", response_model=list[PhotoSchema])
def list_photos(db: Session = Depends(get_db)):
    """
    Retrieves a list of uploaded photos from the database.
    """
    return db.query(Photo).all()
