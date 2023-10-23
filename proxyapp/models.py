from django.db import models


# Original Model

class Employee(models.Model):
    EmployeeType = (
        ("D", "Developer"),
        ("M", "Manager"),
    )
    name = models.CharField(max_length=55)
    type = models.CharField(choices=EmployeeType, max_length=1, default='D')

    def __str__(self):
        return self.name

# Model manager to use in Proxy model

class ManagerEmpManager(models.Manager):

    def get_queryset(self):
        return super(ManagerEmpManager, self).get_queryset().filter(type='M')

    def create(self, **kwargs):
        kwargs.update({'type': 'M'})
        return super(ManagerEmpManager, self).create(**kwargs)


# Proxy Model

class ManagerEmployee(Employee):

    objects = ManagerEmpManager()

    class Meta:
        proxy = True
