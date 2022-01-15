from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model

from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.


class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField()
    def __str__(self):
        return str(self.user.username)


class Complaint(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)


class Rating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)



class BookService(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.TextField()
    wanted_date=models.DateField(default=timezone.now)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin=models.IntegerField()
    accepted='accepted'
    pending='pending'
    rejected='rejected'

    statuses=[
        (accepted,'accepted'),
        (pending,'pending'),
        (rejected,'rejected')
    ]
    status=models.CharField(max_length=50,choices=statuses,default=pending)
    complete=models.BooleanField(default=False)
    price=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    received=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)



class Invoice(models.Model):
    booking=models.ForeignKey(BookService,on_delete=models.CASCADE,null=True,blank=True)
    invoice_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.booking.user.username)
