# Generated by Django 4.0.6 on 2022-07-07 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('hired_date', models.DateTimeField(auto_now_add=True)),
                ('salary', models.IntegerField()),
                ('chief', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.employee')),
            ],
        ),
    ]
