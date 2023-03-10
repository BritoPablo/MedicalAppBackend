from pathlib import Path

from datetime import timedelta #addes to yous with simple_jwt configuration

#ADDED
import os
import environ

env = environ.Env()
environ.Env.read_env()
#####


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DOMAIN = os.environ.get('DOMAIN')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')  #CHENGED

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')  #CHENGED

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')  #CHENGED


# Application definition


#CHANJGED
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
##

#ADDED
PROJECT_APPS = [
    'apps.user',

]
######

#ADDED
THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'djoser',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]
####

#ADDED
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS
####

#ADDED
#CKEditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'autoParagraph' : False
    }
}

CKEDITOR_UPLOAD_PATH = "/media/"
#######


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', #ADDED
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators


#ADDED JWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}
###


#ADDED to manage passwords using argon2 with django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
#######

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/


#CHANGED
LANGUAGE_CODE = 'es'

TIME_ZONE = 'AMERICA/LA_PAZ'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#####




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static') #added
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #added
MEDIA_URL = '/media/' #added

#ADDED
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
######





# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#ADDED
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


AUTH_USER_MODEL = 'user.UserAccount'  #ADDED to point to model user in models.py of user app

CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:5173'] 
##env.list('CORS_ORIGIN_WHITELIST_DEV')

CSRF_TRUSTED_ORIGIN = env.list('CSRF_TRUSTED_ORIGIN_DEV')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
######


#ADDED
DJOSER = {
    'LOGIN_FIELD' : 'email',
    'USER_CREATE_PASSWORD_RETYPE' : True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION' : True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION' : True,
    'SEND_ACTIVATION_EMAIL' : True,
    'SEND_CONFIRMATION_EMAIL' : True,
    'SET_USERNAME_RETYPE' : True,
    'SET_PASSWORD_RETYPE' : True,
    'PASSWORD_RESET_CONFIRM_RETYPE' : True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create' : 'apps.user.serializers.UserSerializer',
        'user' : 'apps.user.serializers.UserSerializer',
        'current_user' : 'apps.user.serializers.UserSerializer',
        'user_delete' : 'djoser.serializers.UserDeleteSerializer',
    },
}
#######



#ADDED
if not DEBUG:
    ALLOWED_HOSTS=env.list('ALLOWED_HOSTS_DEPLOY')

    CSRF_TRUSTED_ORIGIN = env.list('CSRF_TRUSTED_ORIGIN.DEPLOY')
    CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEPLOY')

    DATABASES = {
        "default" : env.db('DATABASE_URL'),
    }
    DATABASES["default"]['ATOMIC_REQUESTS'] = True
########