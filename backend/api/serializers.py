from rest_framework import serializers
from .models import KenyaConflictData

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KenyaConflictData
        fields = '__all__'  # Include all fields from the model
