# Generated by Django 4.0.6 on 2022-07-08 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_alter_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='chief',
        ),
    ]