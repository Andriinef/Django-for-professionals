from os import getenv
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = SRC_DIR.parent


SECRET_KEY = getenv(
    "DJANGO_SECRET_KEY",
    default="django-insecure-^#bh514euy38k9jf^!dzjl*euca)_u5h_dn26ilf!7y7z*0)xh",
)

DEBUG = getenv("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", default="0.0.0.0").split(",")

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": ROOT_DIR / "db.sqlite3",
    # }
    "default": {
        "ENGINE": getenv("DB_ENGINE", default=""),
        "HOST": getenv("DB_HOST", default=""),
        "NAME": getenv("DB_NAME", default=""),
        "USER": getenv("DB_USER", default=""),
        "PASSWORD": getenv("DB_PASSWORD", default=""),
        "PORT": getenv("DB_PORT", default=""),
    }
}

STATIC_URL = "/static/"

STATICFILES_DIRS = [ROOT_DIR / "src/static"]

STATIC_ROOT = ROOT_DIR / "src/staticfiles"

MEDIA_URL = "/media/"

MEDIA_ROOT = ROOT_DIR / "src/media"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local
    "pages.apps.PagesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "django_project.wsgi.application"


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

LANGUAGE_CODE = "uk"

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# .env
DJANGO_SECRET_KEY = "django-insecure-^#bh514euy38k9jf^!dzjl*euca)_u5h_dn26ilf!7y7z*0)xh"

DJANGO_DEBUG = 1

DJANGO_ALLOWED_HOSTS = "localhost,127.0.0.1,*"

# DATABASES
DB_ENGINE = "django.db.backends.postgresql"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres_4"
DB_USER = "andrii"
DB_PASSWORD = "5048"
