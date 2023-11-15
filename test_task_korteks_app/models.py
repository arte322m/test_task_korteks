from django.db import models


class Employee(models.Model):
    surname = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    father_name = models.CharField(max_length=40, null=True, blank=True)
    job_title = models.ForeignKey('JobTitle', on_delete=models.CASCADE, null=True, blank=True)
    employment_date = models.DateField()


class JobTitle(models.Model):
    name = models.CharField(max_length=50)
