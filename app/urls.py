from django.urls import path

from .views import *


urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('complete/<int:pk>/', task_complete, name='complete'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),

    path('subtask/<int:pk>/', SubTaskCreateView.as_view(), name='subtask_create'),
    path('subtask/<int:pk>/update/', SubTaskUpdateView.as_view(), name='subtask_update'),
    path('subtask/<int:pk>/delete', SubTaskDeleteView.as_view(), name='subtask_delete'),
    path('subtask/<int:pk>/complete/', subtask_complete, name='subtask_complete'),

    path('complete_list/<int:pk>/', TaskCompleteListView.as_view(), name='complete_list'),
    path('tomorrow_list/<int:pk>/', TaskTomorrowListView.as_view(), name='tomorrow_list'),
    path('yesterday_list/<int:pk>/', TaskYesterdayListView.as_view(), name='yesterday_list'),
    path('today_list/<int:pk>/', TaskTodayListView.as_view(), name='today_list')
    ]
