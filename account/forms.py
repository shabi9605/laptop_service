from django import forms
from django.db.models.fields import DateField
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput, SelectDateWidget, Widget


class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2')
        labels=('password1','password','password2','confirm password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=('phone',)



class ComplaintForm(forms.ModelForm):
    content=forms.Textarea()
    class Meta:
        model=Complaint
        fields=('content',)


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=('rating',)



class ServiceBookingForm(forms.ModelForm):
    wanted_date=forms.DateField(widget=SelectDateWidget)
    complaint=forms.Textarea()
    class Meta:
        model=BookService
        fields=('complaint','wanted_date','country','state','district','city','pin')



class CustomModelFilter(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.user, obj.price)

class CustomForm(forms.ModelForm):
    booking = CustomModelFilter(queryset=BookService.objects.filter(complete=True))

    class Meta:
        model = Invoice
        fields = ['booking',]