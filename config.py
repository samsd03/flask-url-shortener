import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///urls.db')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev')