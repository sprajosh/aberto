import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        # Database driver
        'ENGINE': 'django.db.backends.sqlite3',
        # Replace below with Database Name if using other database engines
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = ["aberto"]

SECRET_KEY = "built-byno3r6&!p@kt(tjeb6t)2xdr@p8hh24z)#(lhm9e-jz)fl048_6sid"
