# Generated by Django 5.0.1 on 2024-01-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('cpf', models.CharField(max_length=14)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('adress', models.CharField(max_length=150)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('donor', models.BooleanField(default=False)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]