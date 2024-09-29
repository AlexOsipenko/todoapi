from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status']

    ordering_fields = ['title', 'status']
    ordering = ['status']  
    def perform_destroy(self, task):
        if task.status == "completed":
            raise ValidationError("You can't delete completed task")
        task.delete()
