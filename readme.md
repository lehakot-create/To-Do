python manage.py shell

from app.models import *

Category.objects.create(name='Общая')
Category.objects.create(name='Рабочая')

User.objects.create(username='Mike')
User.objects.create(username='Ivan')

Priority.objects.create()
Priority.objects.create(name='Low')
Priority.objects.create(name='High')

Control.objects.create(user=User.objects.get(id=7))

Task.objects.create(title='Финансирование Купцова', category=Category.objects.get(id=2), executor=User.objects.get(id=7), priority=Priority.objects.get(id=3))
Task.objects.create(title='Финансирование Бочаров', category=Category.objects.get(id=2), executor=User.objects.get(id=7), priority=Priority.objects.get(id=1))
Task.objects.create(title='Закупка', category=Category.objects.get(id=2), executor=User.objects.get(id=7), priority=Priority.objects.get(id=1))
Task.objects.create(title='Задача', category=Category.objects.get(id=2), executor=User.objects.get(id=7), priority=Priority.objects.get(id=1))
Task.objects.create(title='Оплатить взнос', text='Оплатить взнос в Мастерскую Талантов за Мишу', category=Category.objects.get(id=2), executor=User.objects.get(id=7), priority=Priority.objects.get(id=1))
