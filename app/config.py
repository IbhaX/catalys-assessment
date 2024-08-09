import os

class Config:
    API_KEY = os.getenv('API_KEY', None)
    LOG_FILE = 'app.log'
