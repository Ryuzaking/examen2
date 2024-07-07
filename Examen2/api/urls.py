from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet
from . import views

router = DefaultRouter()
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tareas/ids/', views.get_all_tareas_ids, name='get_all_tareas_ids'),
    path('tareas/ids-titles/', views.get_all_tareas_ids_titles, name='get_all_tareas_ids_titles'),
    path('tareas/undonetask-ids-titles/', views.get_undonetask_tareas_ids_titles, name='get_undonetask_tareas_ids_titles'),
    path('tareas/donetask-ids-titles/', views.get_donetask_tareas_ids_titles, name='get_donetask_tareas_ids_titles'),
    path('tareas/ids-userids/', views.get_all_tareas_ids_userids, name='get_all_tareas_ids_userids'),
    path('tareas/donetask-ids-userids/', views.get_donetask_tareas_ids_userids, name='get_donetask_tareas_ids_userids'),
    path('tareas/undonetask-ids-userids/', views.get_undonetask_tareas_ids_userids, name='get_undonetask_tareas_ids_userids'),
]
