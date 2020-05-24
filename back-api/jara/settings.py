import os


VERSION = '0.00.1'
SECRET_KEY = os.environ.get('SECRET_KEY', 'insecure-key')


DEBUG = int(os.environ.get('DEBUG', '0'))


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
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    }
}


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]


CORS_ORIGIN_ALLOW_ALL = True


INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'corsheaders'
]


ROOT_URLCONF = 'jara.urls'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


DATABASE_ROUTERS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jara',
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'test'),
        'HOST': os.environ.get('MYSQL_HOST', 'db'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
        'ATOMIC_REQUESTS': False,
        'AUTOCOMMIT': True,
        'CONN_MAX_AGE': 0,
        'TIME_ZONE': None,
        'DISABLE_SERVER_SIDE_CURSORS': False,
        'TEST': {}
    }
}


AUTHENTICATION_BACKENDS = []
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'ORDERING_PARAM': 'sort',
    'DEFAULT_PERMISSION_CLASSES': []
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True

CSRF_COOKIE_SECURE = True
