import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'true').lower() == "true"

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get(
    os.environ.get("DATABASE_URL_CONFIG")))
DEFAULT_CONNECTION.update({"CONN_MAX_AGE": 600})
DATABASES = {"default": DEFAULT_CONNECTION}
ALLOWED_HOSTS = ['*']
