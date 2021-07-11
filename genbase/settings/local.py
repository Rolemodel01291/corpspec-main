from genbase.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'genbase_db',
        'HOST': 'localhost',
    }
}
