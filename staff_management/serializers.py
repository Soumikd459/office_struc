

from rest_framework import serializers
from .models import *
from datetime import datetime

class StaffSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = Staff
        fields = '__all__'  #['status_id','name']