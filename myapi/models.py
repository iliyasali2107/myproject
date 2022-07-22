from django.db import models
from django.forms import IntegerField


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    hired_date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    chief = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    position = models.IntegerField(default=1)

    def __str__(self):
        return self.first_name
    




