# Generated by Django 3.2.16 on 2023-06-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20230613_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='real_name',
            field=models.CharField(default=1, max_length=255, unique=True, verbose_name='真实姓名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='用户名'),
        ),
    ]
