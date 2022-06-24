import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .settings_secret import DJANGO_SECRET_KEY


try:
    sentry_sdk.init(
        # dsn="___",
        integrations=[
            DjangoIntegration(),
        ],
        # si pas indiqué, sentry va chercher la dsn dans les variables d'environnement à SENTRY_DSN.
        # il faudrait trouver un truc comme si pas dsn dans env variables
        # ou si debug on, alors utiliser celle de settings_secret

        traces_sample_rate=1.0,  # 1.0 = 100%
        # captures both error and performance data.
        # To reduce the volume of performance data captured,
        # change traces_sample_rate to a value between 0 and 1.

        send_default_pii=True
    )
except KeyError as e:
    from .settings_secret import SENTRY_DSN
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
        ],
        # si pas indiqué, sentry va chercher la dsn dans les variables d'environnement à
        # SENTRY_DSN.
        # il faudrait trouver un truc comme si pas dsn dans env variables
        # ou si debug on, alors utiliser celle de settings_secret

        traces_sample_rate=1.0,  # 1.0 = 100%
        # captures both error and performance data.
        # To reduce the volume of performance data captured,
        # change traces_sample_rate to a value between 0 and 1.

        send_default_pii=True
    )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1 in development is = True, 0 in environment variables is = False
DEBUG = bool(int(os.environ.get('DEBUG', 1)))

SECRET_KEY = os.environ.get('SECRET_KEY', DJANGO_SECRET_KEY)
# other solution : put 'something_secret' on second position)

ALLOWED_HOSTS = []
ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS.split(','))
    # dans .env : ALLOWED_HOSTS=127.0.0.1, localhost ?

INSTALLED_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lettings',
    'profiles'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
