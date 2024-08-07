
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class postcoursemodel(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    course=models.CharField(max_length=50)
    spec=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    mode=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()

class postvacmodel(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    jobtitle=models.CharField(max_length=20)
    wrktype=models.CharField(max_length=20)
    exp=models.CharField(max_length=30)
    jobtype=models.CharField(max_length=20)
    salary = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone = models.IntegerField()

class applyvacmodel(models.Model):
    cname=models.CharField(max_length=20)
    jobtitle = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email=models.EmailField()
    quali=models.CharField(max_length=20)
    exp=models.CharField(max_length=30)
    phone = models.IntegerField()
    resume = models.FileField(upload_to="admiss/static")

class applycoursemodel(models.Model):
    cname=models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    spec=models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email=models.EmailField()
    quali=models.CharField(max_length=20)
    dob=models.DateField()
    phone = models.IntegerField()
    certi = models.FileField(upload_to="admiss/static")

class teacherregmodel(models.Model):

    uname=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    qualification=models.CharField(max_length=20)
    phone=models.IntegerField()
    password=models.CharField(max_length=20)

class studentregmodel(models.Model):

    uname=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    qualification=models.CharField(max_length=20)
    phnno=models.IntegerField()
    password=models.CharField(max_length=20)

class apprejmodel(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    quali=models.CharField(max_length=20)
    exp=models.CharField(max_length=20)
    jobtitle=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    apprej=models.CharField(max_length=20)
    reason=models.CharField(max_length=20)

class studentapprejmodel(models.Model):
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    quali = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    spec = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    apprej = models.CharField(max_length=20)
    reason = models.CharField(max_length=20)





