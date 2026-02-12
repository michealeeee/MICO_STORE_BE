
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import School
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SchoolSerializer

# Create your views here.
class CreateSchoolAPIView(APIView):
    def post(self,request):
        school_data = SchoolSerializer(data=request.data)
        if school_data.is_valid():
            school_data = school_data.validated_data
            s=School(name=school_data['name'],
                address=school_data['address'],
                country=school_data['country'],
            )
            s.save()
            serialized_data = SchoolSerializer(s)
            return Response({'success':'created a new user','school':serialized_data.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'couldn\'t create the user'}, status=status.HTTP_400_BAD_REQUEST)

class GetSchoolAPIView(APIView):
    def get(self,request,name):
        try:
            s = School.objects.get(name=name)
            serialized_data = SchoolSerializer(s)
            return Response(serialized_data.data,status = 200)
        except School.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
        
class GetAllSchoolAPIView(APIView):
    def get(self,request):
        try:
            s = School.objects.get()
            serialized_data = SchoolSerializer(s,many=True)
            return Response(serialized_data.data,status = 200)
        except School.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
        
class DeleteSchoolAPIView(APIView):
    def delete(self,request,name):
        try:
            s = School.objects.get(name=name)
            s.delete()
            return Response({'success':'user deleted successfully'},status = 200)
        except School.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
        
class UpdateSchoolAPIView(APIView):
    def put(self,request,name):
        try:
            s = School.objects.filter(name=name).first()
            mike_data = SchoolSerializer(data=request.data)
            if mike_data.is_valid():
                    mike_valid_data=mike_data.validated_data
                    s.name=mike_valid_data['name']
                    s.address=mike_valid_data['address']
                    s.country=mike_valid_data['country']
                    s.save()
            return Response({'success':'school updated successfully'},status = 200)
        except School.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
        


        





            
