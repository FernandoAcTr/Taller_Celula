import os

PORT = os.getenv('PORT') or 5000
MONGODB_URI = 'mongodb://127.0.0.1:27017/estacion_climatica'
ENVIRONMENT = os.getenv('ENV') or 'development'
DEBUG = os.getenv('DEBUG') or True
