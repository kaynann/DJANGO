# Generated by Django 5.0.1 on 2024-01-17 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carbohydrate', models.FloatField()),
                ('proteins', models.FloatField()),
                ('fats', models.FloatField()),
                ('calories', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('consumed_food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrion.food')),
            ],
        ),
    ]