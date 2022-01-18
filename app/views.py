from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Task, SubTask, Category
from django.urls import reverse_lazy
from .forms import TaskForm, UserForm, SubTaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    # template_name = 'index.html'
    context_object_name = 'task'
    ordering = ['-priority']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.user.id)

        context['perform_yesterday'] = Task.objects.filter(executor_id=self.request.user.id, status='PE')\
            .filter(date_finish__lt=datetime.today().date()).order_by('-priority', 'date_finish', 'time_finish')

        context['perform_today'] = Task.objects.filter(executor_id=self.request.user.id, status='PE'). \
            filter(date_finish=datetime.today().date()).order_by('-priority')

        # context['perform'] = Task.objects.filter(id=self.request.user.id, status='PE').order_by('-priority')

        context['perform_tomorrow'] = Task.objects.filter(executor_id=self.request.user.id, status='PE')\
            .filter(date_finish=datetime.today().date() + timedelta(days=1)).order_by('-priority')

        context['perform_not_date'] = Task.objects.filter(executor_id=self.request.user.id, status='PE'). \
            filter(date_finish=None).order_by('-priority')

        context['completed'] = Task.objects.filter(executor_id=self.request.user.id, status='CO')

        context['subtask'] = SubTask.objects.filter(executor=self.request.user.id)

        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(id=self.kwargs.get('pk'))
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.executor = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
    context_object_name = 'task'


@login_required
def task_complete(request, pk):
    t = Task.objects.get(id=pk)
    t.date_finish = datetime.today().date()
    t.time_finish = datetime.today().time()
    t.status = 'CO'
    t.save()
    return redirect('task_list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profile.html'
    success_url = reverse_lazy('task_list')
    form_class = UserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.kwargs.get('pk'))
        return context


class SubTaskCreateView(LoginRequiredMixin, CreateView):
    model = SubTask
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task_list')
    form_class = SubTaskForm
    initial = {'title': 'title', 'text': 'text'}

    def form_valid(self, form, **kwargs):
        id = self.kwargs.get('pk')

        form.instance.id_task = Task.objects.get(id=id)
        form.instance.category = Task.objects.get(id=id).category
        form.instance.executor = Task.objects.get(id=id).executor
        form.instance.priority = Task.objects.get(id=id).priority
        return super(SubTaskCreateView, self).form_valid(form)
