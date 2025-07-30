from django.shortcuts import render
from django.views.generic import ListView, DetailView
from task_app.models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'