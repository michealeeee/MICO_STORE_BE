from django.urls import path, include
from .views import home,school
urlpatterns = [
    path('home',home,name="a route that returns welcome message"),
    path('school',school,name=""),

    ]
