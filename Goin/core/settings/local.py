MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]

CREATE_APPS = [
    'apps.products',
    'apps.recommendation',
    'apps.tga',
]

INSTALLED_LIBRARY = [
    'django_filters',
    'jazzmin',
    'rest_framework',
    'drf_yasg',
    "corsheaders",
    'phonenumbers'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS
