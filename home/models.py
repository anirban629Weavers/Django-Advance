from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()
    phone=models.CharField(max_length=11,default="1234567890")
    
class Product(models.Model):
    test=models.CharField(max_length=100)