from django.apps import AppConfig
from mongoengine import connect,disconnect


class MicoStoreApiV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mico_store_api_v1'
    def ready(self):
        disconnect(alias='default')
        connect(db = 'MICOSTOREDB',
                host='mongodb+srv://mke00007_db_user:ofLjBkXKyzGZgYKJ@micostoredb.vs6rvei.mongodb.net/?appName=MICOSTOREDB',)
        