from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yxt4wx!d)rjnyes!vy*purx_aw@-=%o@5$!1%0!ygfr_er3!*p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#INSTALLED_APPS = []


#site freamwork
SITE_ID = 2
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
] 

X_FRAME_OPTIONS = "SAMEORIGIN"
