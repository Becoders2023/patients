from django.db import models

class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.models.CharField(max_length=10)
    address=models.TextField()
    medical_history=models.TextField