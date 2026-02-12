from django.apps import AppConfig
from mongoengine import connect, disconnect


# class MensahConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'mensah'
#     def ready(self):
#         disconnect(alias='default')
#         connect(db = 'Ken',
#                 host='mongodb+srv://mke00007_db_user:ofLjBkXKyzGZgYKJ@Ken.vs6rvei.mongodb.net/?appName=Ken',)