from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('complete/<int:pk>/', task_complete, name='complete'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('subtask/<int:pk>', SubTaskCreateView.as_view(), name='subtask_create'),
    ]
