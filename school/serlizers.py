from dataclasses import field
from school.models import  student
from rest_framework import serializers



class studentserlizer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

    
