import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    APP_NAME = "AI Image Processor"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

    # JWT Authentication
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # Payment (Stripe)
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "your_stripe_key")

    # Email Notifications (SendGrid)
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "your_sendgrid_key")

config = Config()
