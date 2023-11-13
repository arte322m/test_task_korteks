from django.db import models


class Employees(models.Model):
    firstname = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    father_name = models.CharField(max_length=40, null=True)
    post = models.ForeignKey('JobTitle', on_delete=models.CASCADE)
    employment_date = models.DateField()


class JobTitle(models.Model):
    name = models.CharField(max_length=50)
