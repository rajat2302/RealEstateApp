# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p8=bzwng)a#oc9y1clolqr2^ps!7z+lv5tdfrk-#0$ebn7k2^2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'dbadmin',
        'PASSWORD': 'abc123!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Email config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rajat.pandey@sitpune.edu.in'
EMAIL_HOST_PASSWORD= 'Prime@2302'
EMAIL_USE_TLS=True

