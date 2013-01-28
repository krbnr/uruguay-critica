import os
gettext = lambda s: s

PROJECT_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), '..')
print
def rel(*x):
    return os.path.join(PROJECT_ROOT, *x)
"""Check if this line make d=the media dir workable"""


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('kelian', 'kelian.puppi@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'uruguaycritica.db',
        'USER': '',                      
        'PASSWORD': '',                  
        'HOST': 'localhost',                      
        'PORT': '',                      
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('collectedstatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static'),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

PIPELINE = False

SECRET_KEY = 's1n95nhab_lj%7u*lkb8i6+3-t7ez-39#)c+5@hdjc7a)t!&amp;1i'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'uruguay_critica.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'uruguay_critica.wsgi.application'

TEMPLATE_DIRS = (
    rel('templates'),
    rel('main/templates'),
    rel('critics/templates'),
)


AUTH_PROFILE_MODULE = '../critics.critic'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'sekizai',
    'main',
    'critics',
    'south',

)


CMS_TEMPLATES = (
    ('base.html', 'Base'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}