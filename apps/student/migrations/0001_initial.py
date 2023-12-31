# Generated by Django 3.2.16 on 2023-06-13 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, verbose_name='班级名称')),
                ('location', models.CharField(max_length=255, verbose_name='上课地点')),
                ('level', models.CharField(max_length=20, verbose_name='等级')),
                ('is_delete', models.BooleanField(default=False)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rbac_class',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('sex', models.CharField(max_length=11, verbose_name='性别')),
                ('telephone', models.CharField(max_length=11, verbose_name='电话')),
                ('subject', models.CharField(max_length=255, verbose_name='科目')),
                ('grade', models.CharField(max_length=10, verbose_name='年级')),
                ('school', models.CharField(max_length=100, null=True, verbose_name='学校')),
                ('is_delete', models.BooleanField(default=False)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.class')),
            ],
            options={
                'db_table': 'rbac_student',
            },
        ),
    ]
