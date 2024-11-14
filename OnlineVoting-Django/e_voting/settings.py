"""
Django settings for e_voting project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%6lp_p!%r$7t-2ql5hc5(r@)8u_fc+6@ugxcnz=h=b(fn#3$p9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*","localhost","172.16.1.15", "127.0.0.1", "cpuevoting.com", "www.cpuevoting.com","www.cpuevoting.com:8800","e335-210-23-168-187.ngrok-free.app"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    # My Created Applications
    'acc.apps.AccountConfig',
    'voting.apps.VotingConfig',
    'administrator.apps.AdministratorConfig',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',  # Add this line
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # 'acc.middleware.AccountCheckMiddleWare',
    # "allauth.account.middleware.AccountMiddleware", #add this
]

ROOT_URLCONF = 'e_voting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 'voting/templates', 'administrator/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'voting.context_processors.ElectionTitle'
            ],
        },
    },
]

WSGI_APPLICATION = 'e_voting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # #   You can use this :
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }

 
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'e_voting',  # Replace with your actual database name
        'USER': 'sa',      # XAMPP uses 'root' by default for MySQL
        'PASSWORD': 'p@ssw0rd',      # XAMPP's MySQL 'root' user has no password by default, but add one if you’ve set it
        'HOST': 'localhost', # This points to your local MySQL server in XAMPP
        'PORT': '3306',      # Default MySQL port in XAMPP
    }


}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'  # Set to your desired timezone
USE_TZ =  False

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

AUTH_USER_MODEL = 'acc.CustomUser'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '850437372061-ebnf96svh3p387ciekeh9upgvgni9381.apps.googleusercontent.com',
            'secret': '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',
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True,
    },
    'github': {
        'APP': {
            'client_id': '',
            'secret': '',
        }
    }
}


SOCIALACCOUNT_ADAPTER = 'acc.adapter.CustomSocialAccountAdapter'



AUTHENTICATION_BACKENDS = ['acc.email_backend.EmailBackend']
# AUTHENTICATION_BACKENDS = [
 
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',

#     # `allauth` specific authentication methods, such as login by email
#     'allauth.account.auth_backends.AuthenticationBackend',
  
# ]

SITE_ID = 1
# Redirect URLs
LOGIN_REDIRECT_URL = '/'  # Redirect after login
LOGOUT_REDIRECT_URL = '/'  # Redirect after logout



ELECTION_TITLE_PATH = os.path.join(
    BASE_DIR, 'election_title.txt')  # Election Title File

SEND_OTP = False  # If you toggle this to False, Kindly use 0000 as your OTP
