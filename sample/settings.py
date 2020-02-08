"""
Django settings for sample project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
from dotenv import (
    load_dotenv,
)
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

certificate_text = open("rsa_certificates/certificate.pem", 'rb').read()
certificate = load_pem_x509_certificate(certificate_text, default_backend())
default_publickey = certificate.public_key()

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'sample',
    'rest_framework_jwt',
    'rest_framework_auth0',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_auth0.authentication.Auth0JSOAuthorizationNWebTokenAuthentication',
    # ),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[{}] [%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] [%(funcName)s] %(message)s".format(str(os.environ['LOGGER_APPLICATION_NAME'])),
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': sys.stdout
        },
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'standard',
            'facility': 'user',
            # uncomment next line if rsyslog works with unix socket only (UDP reception disabled)
            # 'address': '/dev/log'
        }
    },
    'loggers': {
        # Logger must be called django
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['console'],
        },
        'rest_framework_auth0': {
            'handlers': ['console', 'syslog'],
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
        os.environ.get('LOGGER_APPLICATION_NAME'): {
            'handlers': ['console', 'syslog'],
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    }
}

AUTH0 = {
    'CLIENTS': {
        'default': {
            'AUTH0_CLIENT_ID': os.environ.get('AUTH0_CLIENT_ID'),  #make sure it's the same string that aud attribute in your payload provides
            'AUTH0_CLIENT_SECRET': os.environ.get('AUTH0_CLIENT_SECRET'),
            'CLIENT_SECRET_BASE64_ENCODED': eval(
                os.environ.get('AUTH0_CLIENT_SECRET_BASE64_ENCODED', 'False')
            ),
            'AUTH0_AUDIENCE': os.environ.get('AUTH0_AUDIENCE'),
            'AUTH0_ALGORITHM': 'RS256',  # default used in Auth0 apps
            'PUBLIC_KEY': default_publickey,
        }
    },
    # Optional
    # 'AUTH_COOKIE_NAME': None,  # if you want to use cookie instead of header, set this setting
    # 'AUTHORIZATION_EXTENSION': False,  # default to False
    # 'USERNAME_FIELD': 'sub',
    # 'CLIENT_CODE_HEADER': 'Client_Code',
    # 'AUTH_HEADER_PREFIX': 'Bearer',  # default prefix used by Auth0 lock.js
    # 'REPLACE_PIPE_FOR_DOTS_IN_USERNAME': True,
    # 'GET_USERNAME_HANDLER':
    # 'rest_framework_auth0.utils.get_username_from_payload',
}

CORS_ORIGIN_ALLOW_ALL = True #Just for test, don't use in production
