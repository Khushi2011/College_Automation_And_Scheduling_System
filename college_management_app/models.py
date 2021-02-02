from django.db import models

# Create your models here.
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    gender=models.CharField(max_length=6)
    address=models.TextField()
class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    gender=models.CharField(max_length=6)
    address=models.TextField()
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    gender=models.CharField(max_length=6)
    address=models.TextField()
 
