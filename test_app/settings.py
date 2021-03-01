import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
USE_TZ = True
SITE_ID = 1
SECRET_KEY = 'keepitsecretkeepitsafe'
STATIC_URL = '/static/'

ROOT_URLCONF = 'test_app.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',  # must come after south to override south's test command
    'django_rpx_plus',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ('--nocapture', )

if 'migrate' in sys.argv or 'schemamigration' in sys.argv or (
        'syncdb' in sys.argv):
    INSTALLED_APPS += ('south',)

SILENCED_SYSTEM_CHECKS =[
    'admin.E403',  # ignore missing TEMPLATES
    'admin.E408',  # Ignore missing AuthenticationMiddleware
    'admin.E409',  # Ignore missing MessageMiddleware
    'admin.E410',  # Ignore missing SessionMiddleware
]