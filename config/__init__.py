"""Centralizes application settings for development and production."""

import os                                             
"""gives Python access to operating-system environment variables."""
from dotenv import load_dotenv


load_dotenv()
"""eads your local .env file and makes its variables available to Python."""

class Config:
    """groups related settings in one place."""

    APP_ENV = os.getenv("APP_ENV", "development")
    """reads APP_ENV, using "development" if the variable isn't set."""
    SECRET_KEY = os.getenv("SECRET_KEY")
    """reads the secret key from the environment."""