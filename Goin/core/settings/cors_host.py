CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = ('content-disposition', 'accept-encoding',
                      'content-type', 'accept', 'origin', 'Authorization', 'access-control-allow-methods')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:3080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:4040",
]
CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
LOCAL_HOST = ['*']
ALLOWED_HOSTS = LOCAL_HOST + CORS_ALLOWED_ORIGINS

