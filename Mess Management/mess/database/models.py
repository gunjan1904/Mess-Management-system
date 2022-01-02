from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.
class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    roll_num = models.ForeignKey(User, db_column="username", unique=True, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Number = models.CharField(max_length=10)
    Address = models.CharField(max_length=80)
    Email = models.EmailField(max_length=30, unique=True)
    #image = models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=100, null=True)

Gender_choices=(('M', 'Male'),('F', 'Female'))
class MessWorker(models.Model):
    WorkerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30) 
    Number = models.CharField(max_length=10)
    Gender = models.CharField(max_length=1, choices=Gender_choices, default='M')
    Address = models.CharField(max_length=80)
    Document = models.FileField(upload_to='documents', blank=True)
 
class MessMenu(models.Model):
    menu = models.FileField(upload_to='mess_menu')

class Coupon(models.Model):
    Coupon_ID = models.AutoField(primary_key=True) 
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Date = models.DateField(default=None)
    Breakfast = models.IntegerField(default=0)
    Lunch = models.IntegerField(default=0)
    Evening_snacks = models.IntegerField(default=0)
    Dinner = models.IntegerField(default=0)

Status_choices=(('Not seen', 'Not seen'),('seen', 'seen'))
class ComplaintRecord(models.Model):
    Complaint_ID = models.AutoField(primary_key=True)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
    Subject=models.TextField(max_length=50, default="")
    Description = models.TextField(max_length=200)
    Status = models.CharField(max_length=20, choices=Status_choices ,default='Not seen')
    Comments = models.CharField(max_length=30, default="", blank=True)
   

    