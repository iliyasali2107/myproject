from turtle import position
from myproject.wsgi import get_wsgi_application
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()

from faker import Faker
from myapi.models import Employee
import random
import math

def roundup(x):
    return int(math.ceil((500 - x) / 100)) * 100

def rounddown(x):
    return math.floor((500 - x)/100)*100

fake = Faker()

size = Employee.objects.all().count()
# emp = Employee.objects.all()
first_chief = Employee.objects.first()

for i in range(2,501):
    

    first_name = fake.first_name()
    last_name = fake.last_name()
    position = math.ceil(i / 100)
    if i <= 100:
        chief = first_chief
        salary = random.randint(400, 500)
    else:
        chief = Employee.objects.get(id=(i-100))
        salary = random.randint(rounddown(i),roundup(i))
    

    emp = Employee(first_name=first_name, last_name=last_name, salary=salary, chief = chief, position = position)
    emp.save()
    size += 1
    
    
    
    
    # Employee.objects.get(id=i).delete()    
    
    









