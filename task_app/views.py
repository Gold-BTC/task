from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from task_app.forms import TaskForm
from task_app.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task_list.html'
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'task_detail.html'

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'task_create.html'
    success_url = reverse_lazy("task_list")
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'task_update.html'
    success_url = reverse_lazy("task_list")
    form_class = TaskForm