import os

PORT = os.getenv('PORT') or 5000
#MONGODB_URI = 'mongodb://127.0.0.1:27017/estacion_climatica'
MONGODB_URI = 'mongodb+srv://python:T5tUY2SDi0FddBeq@cluster0.11cau.mongodb.net/estacion_climatica?retryWrites=true&w=majority'
ENVIRONMENT = os.getenv('ENV') or 'development'
DEBUG = os.getenv('DEBUG') or True
