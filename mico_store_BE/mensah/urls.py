from django.urls import path, include
from .views import CreateSchoolAPIView,GetSchoolAPIView,GetAllSchoolAPIView,DeleteSchoolAPIView,UpdateSchoolAPIView
urlpatterns = [
   path('school/create',CreateSchoolAPIView.as_view(),name="An API that creates a school"),
   path('school/get/<name>',GetSchoolAPIView.as_view(),name="An API that get a school"),
   path('school/all',GetAllSchoolAPIView.as_view(),name="An API that gets all school"),
   path('school/delete/<name>',DeleteSchoolAPIView.as_view(),name="An API that delete all school"),
   path('school/update/<name>',UpdateSchoolAPIView.as_view(),name="An API that update all school"),
   
    ]
