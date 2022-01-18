# Generated by Django 4.0.1 on 2022-01-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='control',
        ),
        migrations.AddField(
            model_name='subtask',
            name='status',
            field=models.CharField(choices=[('PE', 'Выполняется'), ('CO', 'Выполнено')], default='PE', max_length=11),
        ),
    ]