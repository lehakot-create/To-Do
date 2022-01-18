from django.forms import ModelForm, DateField, DateInput, TimeField, TimeInput
from .models import Task, SubTask
from django.contrib.auth.models import User
from datetime import datetime


class TaskForm(ModelForm):
    date_finish = DateField(label='Дата:',
                            widget=DateInput(attrs={'type': 'date'}),
                            initial=datetime.today().date())
    time_finish = TimeField(label='Время:',
                            widget=TimeInput(attrs={'type': 'time'}),
                            initial=datetime.today().time())

    class Meta:
        model = Task
        fields = ['title', 'text', 'date_finish', 'time_finish',
                  'category', 'priority']


class SubTaskForm(ModelForm):
    date_finish = DateField(label='Дата:',
                            widget=DateInput(attrs={'type': 'date'}),
                            initial=datetime.today().date())
    time_finish = TimeField(label='Время:',
                            widget=TimeInput(attrs={'type': 'time'}),
                            initial=datetime.today().time())

    class Meta:
        model = SubTask
        fields = ['title', 'text', 'date_finish', 'time_finish']


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']
