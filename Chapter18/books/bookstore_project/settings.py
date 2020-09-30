"""
Django settings for bookstore_project project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import socket
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('ENV') == 'development' else False

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',    # whitenoise (3rd party)
    'django.contrib.staticfiles',
    'django.contrib.sites',             # added

    # 3rd Party
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'debug_toolbar',

    # Local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'books.apps.BooksConfig',
    'orders.apps.OrdersConfig',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'bookstore_project.urls'

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

WSGI_APPLICATION = 'bookstore_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
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

# Customizations

# Static files dir
# dev
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# prod
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDER = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media Settings
# url we can use in templates:
MEDIA_URL = '/media/'
# user uploaded media goes in:
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'

# Custom Login behavior
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django-allauth config
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SITE_ID = 1
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com'

# https://app.sendgrid.com/guide/integrate
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_PASSWORD')
EMAIL_PORT = 587  # 25, 587  (for unencrypted/TLS connections)
EMAIL_USE_TSL = True

# Stripe
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')

# django-debug-toolbar
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + '1' for ip in ips]

# Cache setup
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800   # 1 week
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Production
if os.environ.get('ENV') == 'production':
    # Force browser to enable XXS filter
    SECURE_BROWSER_XSS_FILTER = True
    # No clickjacking
    X_FRAME_OPTIONS = 'DENY'
    # SSL
    SECURE_SSL_REDIRECT = True
    # HTTP Strict Transport Security
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # Defer browser from interpreting content
    SECURE_CONTENT_TYPE_NOSNIFF = True
    # Cookies only over HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
