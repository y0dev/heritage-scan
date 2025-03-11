from fastapi import FastAPI
from database import engine, Base
from components.photos.routes.photo_routes import router as photo_router

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(photo_router, prefix="/photos", tags=["Photos"])

@app.get("/")
def root():
    return {"message": "Welcome to the Photo Digitization API"}