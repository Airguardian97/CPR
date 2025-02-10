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
# DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost','aims.dns-dynamic.net','aims.dns-dynamic.net','165.154.233.152','cpurv2.cloudns.be','167.86.70.32']






# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
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
        'USER': 'cpuvoting',      # XAMPP uses 'root' by default for MySQL
        'PASSWORD': '12345J@s0np@ssw0rd',      # XAMPP's MySQL 'root' user has no password by default, but add one if you’ve set it
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


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.1/howto/static-files/
# # Static files (CSS, JavaScript, images)
# STATIC_URL = '/static/'

# # Define additional directories to search for static files (e.g., for custom static files in 'static' folder)
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),  # Your static files directory
# ]

# # This is where the collected static files will be stored for production (e.g., for 'collectstatic')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Using Whitenoise for static file serving in production
# # It allows Django to serve static files efficiently in production
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # Whitenoise settings (optional, for extra configuration of file handling, compression, etc.)
# # Add this to enable caching and compression of static files
# WHITENOISE_MAX_AGE = 31536000  # One year in seconds (caching duration for static files)
# WHITENOISE_USE_FINDERS = True  # Enable finding files using Django's staticfinders

# # Media files (uploads from users, etc.)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Define the root folder for media (uploads)

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

if DEBUG:

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

else:

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




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

SESSION_COOKIE_AGE = 3000

LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # TLS for port 587, SSL would be port 465
EMAIL_HOST_USER = 'cpuonlinevoting@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'uzptimkdmdhscfib'  # Use the App Password generated in your Google account
DEFAULT_FROM_EMAIL = 'cpuonlinevoting@gmail.com'  # The default sender email address
