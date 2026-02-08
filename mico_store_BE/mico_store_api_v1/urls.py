from django.urls import path, include
from .views import CreateUserAPIView, GetUserAPIView

urlpatterns = [
    path('create/mike',CreateUserAPIView.as_view(),name="An API that creates a user"),
    path('get/<name>',GetUserAPIView.as_view(),name="An API that gets a user"),
    ]
