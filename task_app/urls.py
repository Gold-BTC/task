# urls.py
from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create', views.TaskCreateView.as_view(), name = 'task_create'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(), name='task_update'),

]