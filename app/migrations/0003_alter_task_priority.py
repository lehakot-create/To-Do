# Generated by Django 4.0.1 on 2022-01-12 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(default='Normal', on_delete=django.db.models.deletion.CASCADE, to='app.priority'),
        ),
    ]
