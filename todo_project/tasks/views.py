from django.shortcuts import render
from rest_framework import viewsets  
from rest_framework.exceptions import ValidationError  
from .models import Task  
from .serializers import TaskSerializer  


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer 

    def perform_destroy(self, task):
        if task.status == 'completed': 
            raise ValidationError("You can't delete completed task") 
        task.delete() 
