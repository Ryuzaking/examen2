from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Tasks
from .serializers import TaskSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

def get_all_tareas_ids(request):
    tareas = Tasks.objects.values_list('id', flat=True)
    return JsonResponse(list(tareas), safe=False)

def get_all_tareas_ids_titles(request):
    tareas = Tasks.objects.values('id', 'title')
    return JsonResponse(list(tareas), safe=False)

def get_undonetask_tareas_ids_titles(request):
    tareas = Tasks.objects.filter(donetask=False).values('id', 'title')
    return JsonResponse(list(tareas), safe=False)

def get_donetask_tareas_ids_titles(request):
    tareas = Tasks.objects.filter(donetask=True).values('id', 'title')
    return JsonResponse(list(tareas), safe=False)

def get_all_tareas_ids_userids(request):
    tareas = Tasks.objects.values('id', 'user_id')
    return JsonResponse(list(tareas), safe=False)

def get_donetask_tareas_ids_userids(request):
    tareas = Tasks.objects.filter(donetask=True).values('id', 'user_id')
    return JsonResponse(list(tareas), safe=False)

def get_undonetask_tareas_ids_userids(request):
    tareas = Tasks.objects.filter(donetask=False).values('id', 'user_id')
    return JsonResponse(list(tareas), safe=False)
