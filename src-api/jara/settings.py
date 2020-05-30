import os


VERSION = '0.00.1'
SECRET_KEY = os.environ.get('SECRET_KEY', 'insecure-key')


DEBUG = int(os.environ.get('DEBUG', '0'))


ROOT_URLCONF = 'jara.urls'


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    }
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware'
]


CORS_ORIGIN_ALLOW_ALL = True


INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'corsheaders',
    'api.users'
]


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher'
]


DATABASES = {
    'default': {
        'NAME': 'jara',
        'ENGINE': 'django.db.backends.mysql',
        'USER': os.environ.get('MYSQL_USER', 'django'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'test'),
        'HOST': os.environ.get('MYSQL_HOST', 'db'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
        'TEST': {},
        'ATOMIC_REQUESTS': False,
        'AUTOCOMMIT': True,
        'CONN_MAX_AGE': 0,
        'TIME_ZONE': None,
        'DISABLE_SERVER_SIDE_CURSORS': False
    }
}


REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'ORDERING_PARAM': 'sort',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'api.library.authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True
