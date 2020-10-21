from .base_settings import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'retention_data_pipeline'
]

EDW_SERVER = 'edw'

if os.getenv("ENV") == "localdev":
    DEBUG = True
    EDW_USER = os.getenv("EDW_USER")
    EDW_PASSWORD = os.getenv("EDW_PASSWORD")
