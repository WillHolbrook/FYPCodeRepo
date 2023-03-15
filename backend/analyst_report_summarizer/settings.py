# -*- coding: utf-8 -*-
"""
Django settings for analyst_report_summarizer project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import socket
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3fh7v7jbzvl#+av2)u+i*#7wz&4uxd159thd)z@0dm%q7@523d"

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("DEBUG") == "False":
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
    "localhost",
    ".willholbrook.com",
    ".willholbrook.com",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_api_key",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "analyst_report_summarizer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "analyst_report_summarizer.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if os.getenv("DJANGO_DATABASE_TYPE") == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "db",
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "/usr/local/www/documents"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Set allowed CSRF Origins
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",  # Dev
    "http://127.0.0.1:3000",  # Dev
    "http://localhost:8020",  # Dev
    "http://localhost:8010",  # Dev
    "http://localhost:8080",  # Dev
    "http://localhost:3000",  # Dev
    "http://fypfrontend.willholbrook.com",  # Prod
    "https://fypfrontend.willholbrook.com",  # Prod
]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_NAME = "XSRF-TOKEN"
CSRF_HEADER_NAME = "HTTP_X_XSRF_TOKEN"

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = CSRF_TRUSTED_ORIGINS

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "PAGE_SIZE": 10,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}

MEDIA_ROOT = BASE_DIR.joinpath("./media")
MEDIA_URL = "/media/"

TEST_RESOURCES_ROOT = BASE_DIR.joinpath("./api/tests/resources/")
if os.getenv("GROBID_SERVER_HOSTNAME"):
    GROBID_SERVER = (
        f"http://{socket.gethostbyname(os.getenv('GROBID_SERVER_HOSTNAME'))}:8070"
    )
else:
    GROBID_SERVER = "http://localhost:8020"

GROBID_CONFIG = {
    "grobid_server": GROBID_SERVER,
    "batch_size": 1000,
    "sleep_time": 10,
    "timeout": 60,
    "coordinates": ["persName", "figure", "ref", "biblStruct", "formula", "s"],
}

X_FRAME_OPTIONS = "ALLOWALL"

DATETIME_TEST_LEEWAY = 10
DEFAULT_MAX_PROCESSES = 8
MIN_REPORTS_MULTIPROCESSING = 10

if DEBUG:
    LOGGING = {
        "version": 1,
        "formatters": {
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        "handlers": {
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            }
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": True,
            },
        },
    }
else:
    LOGGING = {
        "version": 1,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            }
        },
        "handlers": {
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": "/var/log/django/backend.log",
                "formatter": "verbose",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": True,
            },
        },
    }
