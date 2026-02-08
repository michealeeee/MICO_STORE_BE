from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.

class CreateUserAPIView(APIView):
    def post(self,request):
        mike_data = UserSerializer(data=request.data)
        if mike_data.is_valid():
            mike_valid_data=mike_data.validated_data
            u=User(name=mike_valid_data['name'],
                   age=mike_valid_data['age'],
                   email=mike_valid_data['email']                                                       
                   )
            u.save()
            return Response({'success':'created a new user'},status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'couldn\'t create the user'}, status=status.HTTP_400_BAD_REQUEST)

class GetUserAPIView(APIView):
    def get(self,request,name):
        try:
            u = User.objects.get(name=name)
            serialized_data = UserSerializer(u)
            return Response(serialized_data.data,status = 200)
        except User.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
