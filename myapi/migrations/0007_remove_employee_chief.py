# Generated by Django 4.0.6 on 2022-07-09 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_employee_chief'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='chief',
        ),
    ]
