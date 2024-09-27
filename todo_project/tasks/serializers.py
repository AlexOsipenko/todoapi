from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate_status(self, value):
        if value not in ['in_process', 'completed', 'cancelled']:
            raise serializers.ValidationError("status not found")
        return value