INSTALLED_APPS = (
    'django_barcode',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_barcode_testing',
    }
}
SECRET_KEY = "django_barcode_secret_key_for_testing"