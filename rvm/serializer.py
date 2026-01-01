from rest_framework import serializers
from .models import RVM

class RVMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RVM
        fields = ["id", "machine_code", "location_name", "status", ]