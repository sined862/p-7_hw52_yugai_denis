# Generated by Django 4.1.1 on 2022-09-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('status', models.CharField(default='new', max_length=15, verbose_name='Статус')),
                ('date_deadline', models.CharField(default='', max_length=10, verbose_name='Дата выполнения')),
            ],
        ),
    ]