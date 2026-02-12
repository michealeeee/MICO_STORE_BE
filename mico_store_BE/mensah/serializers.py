from .models import School
from rest_framework_mongoengine import serializers

class SchoolSerializer(serializers.DocumentSerializer):
    class Meta:
       model = School
       fields = '__all__'

