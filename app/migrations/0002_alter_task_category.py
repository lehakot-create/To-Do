# Generated by Django 4.0.1 on 2022-01-12 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default='Общая', on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
