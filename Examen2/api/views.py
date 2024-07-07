from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Tasks
from .serializers import TaskSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer