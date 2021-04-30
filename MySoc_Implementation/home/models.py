from django.db import models

# Create your models here.
class Contact (models.Model):
    Name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    appartment=models.CharField(max_length=10)
    password=models.CharField(max_length=40)
    date=models.DateField()

    def __str__(self):
        return self.Name


class Complaint (models.Model):
    ownername=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    appartment=models.CharField(max_length=10)
    desc=models.CharField(max_length=500)
    compNo=models.CharField(max_length=30 , null=True )
    Status=models.CharField(max_length=50 , default="Pending")
    date=models.DateField()
    
    def __str__(self):
        return self.ownername

class Bills (models.Model):
    billno=models.CharField(max_length=10)
    amount=models.CharField(max_length=10)
    issuedate=models.DateField()
    paiddate=models.DateField()
    appartment=models.CharField(max_length=10)
    username1=models.CharField(max_length=30 , null=True)
    Status=models.CharField(max_length=50 , default="Pending")

    def _str_(self):
        return self.billno


class Dependents (models.Model):
    name=models.CharField(max_length=122)
    ownerid=models.CharField(max_length=10)
    appartment=models.CharField(max_length=10)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=122)
    
    def _str_(self):
        return self.name
    

    def _str_(self):
        return self.billno

class Employee (models.Model):
    employeeid=models.CharField(max_length=10)
    name=models.CharField(max_length=122)
    salamount=models.CharField(max_length=10)
    salstatus=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    desc=models.CharField(max_length=122)

    def _str_(self):
        return self.name

class Appartment (models.Model):
    appartmentno=models.CharField(max_length=10)
    ownerid=models.CharField(max_length=10)
    size=models.CharField(max_length=15)
    dependentsno=models.CharField(max_length=15)
    vacancy=models.CharField(max_length=20)

    def _str_(self):
        return self.appartmentno

class Visitor (models.Model):
    name=models.CharField(max_length=30)
    arrival=models.DateTimeField()
    departure=models.DateTimeField()
    ownerid=models.CharField(max_length=10)
    phone=models.CharField(max_length=12)

    def _str_(self):
        return self.name
    