import os

class Config:
    """
    Configuration class for the application.
    
    This class holds configuration variables that can be used throughout the application.
    It uses environment variables for sensitive information and provides default values
    where appropriate.
    """
    
    # API key for external service, retrieved from environment variable
    API_KEY = os.getenv('API_KEY', None)
    
    # File path for application logs
    LOG_FILE = 'app.log'
