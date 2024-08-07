from django import forms
from .models import *




class postcourseform(forms.Form):
    uname = forms.CharField(max_length=20)
    email = forms.EmailField()
    course = forms.CharField(max_length=50)
    spec = forms.CharField(max_length=50)
    duration = forms.CharField(max_length=50)
    mode = forms.CharField(max_length=50)
    fee = forms.CharField(max_length=50)
    eligibility = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    phone = forms.IntegerField()




class postvacform(forms.Form):
    uname=forms.CharField(max_length=20)
    email=forms.EmailField()
    jobtitle=forms.CharField(max_length=20)
    wrktype=forms.CharField(max_length=20)
    exp=forms.CharField(max_length=30)
    jobtype=forms.CharField(max_length=20)
    salary = forms.CharField(max_length=50)
    eligibility = forms.CharField(max_length=1000)
    address =forms.CharField(max_length=1000)
    phone = forms.CharField(max_length=20)



class applyform(forms.Form):
    cname = models.CharField(max_length=20)
    jobtitle = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    quali = models.CharField(max_length=20)
    exp = models.CharField(max_length=30)
    phone = models.IntegerField()
    resume = models.FileField(upload_to="admiss/static")

class courseform(forms.Form):
    cname = forms.CharField(max_length=20)
    course = forms.CharField(max_length=20)
    spec = forms.CharField(max_length=20)
    uname = forms.CharField(max_length=20)
    email = forms.EmailField()
    quali = forms.CharField(max_length=20)
    dob = forms.DateField()
    phone = forms.IntegerField()
    certi =forms.FileField()

class teacherregform(forms.Form):
    uname = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    dob = forms.DateField()
    qualification = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)


class teacherlogform(forms.Form):
    email = forms.EmailField()  # name attribute
    pas = forms.CharField(max_length=20)


class studentregform(forms.Form):
    uname = forms.CharField(max_length=20)
    email = forms.EmailField()
    phnno = forms.CharField(max_length=20)
    dob = forms.DateField()
    qualification = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)


class studentlogform(forms.Form):
    email = forms.EmailField()  # name attribute
    pas = forms.CharField(max_length=20)


class mailform(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'row': 3, 'col': 30}))



class apprejform(forms.Form):
    uname = forms.CharField(max_length=20)
    email = forms.EmailField()
    quali = forms.CharField(max_length=20)
    exp =forms.CharField(max_length=20)
    jobtitle = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    apprej = forms.CharField(max_length=20)
    reason = forms.CharField(max_length=20)


class studentapprejform(forms.Form):
    uname = forms.CharField(max_length=20)
    email = forms.EmailField()
    quali = forms.CharField(max_length=20)
    course = forms.CharField(max_length=20)
    spec = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    apprej = forms.CharField(max_length=20)
    reason = forms.CharField(max_length=20)