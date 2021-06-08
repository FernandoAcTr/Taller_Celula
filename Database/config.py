import os

PORT = os.getenv('PORT') or 5000
MONGODB_URI = 'mongodb://python:tallerCelula123#@cluster0-shard-00-00.11cau.mongodb.net:27017,cluster0-shard-00-01.11cau.mongodb.net:27017,cluster0-shard-00-02.11cau.mongodb.net:27017/taller_celula?ssl=true&replicaSet=atlas-hkx6ie-shard-0&authSource=admin&retryWrites=true&w=majority'
ENVIRONMENT = os.getenv('ENV') or 'development'
DEBUG = os.getenv('DEBUG') or True
