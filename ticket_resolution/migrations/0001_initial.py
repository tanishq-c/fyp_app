# Generated by Django 3.0.5 on 2022-11-07 10:41

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(blank=True, max_length=255)),
                ('emp_uid', models.IntegerField()),
                ('emp_pwd', models.CharField(blank=True, max_length=255)),
                ('dept_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_email', models.CharField(blank=True, max_length=255)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('dept_id', models.IntegerField()),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
