import os
from decouple import config as env
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = env('DEBUG', cast=bool)
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default='0.0.0.0').split()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
from .base import *
