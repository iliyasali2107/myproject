from turtle import position
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics, filters
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.renderers import JSONRenderer



class ListEmployee(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.SearchFilter,)

    search_fields = ("first_name", "last_name", "position", "chief__id")

class DetailEmployee(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    filter_backends = (filters.SearchFilter,)

    search_fields = ("first_name", "last_name")

    def get_default_renderer(self, view):
        return JSONRenderer()
    