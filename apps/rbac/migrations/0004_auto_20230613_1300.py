# Generated by Django 3.2.16 on 2023-06-13 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20230613_1241'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='permissions',
            table='rbac_permissions',
        ),
        migrations.AlterModelTable(
            name='role',
            table='rbac_role',
        ),
    ]
