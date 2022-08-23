from dataclasses import fields
from django import forms
from .models import Employee,Contact
from django.contrib.auth.models import User

GENDER_CHOICE = (("Male", "Male"), ("Female", "Female"))

class EmployeeForm(forms.ModelForm):
    Gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICE))
    class Meta:
        model=Employee
        fields="__all__"
        widgets={
            'empid':forms.NumberInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),     
            'Gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'DOB':forms.DateInput(attrs={'class':'form-control'}),
            'Age':forms.NumberInput(attrs={'class':'form-control'}),
            'Mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'City':forms.TextInput(attrs={'class':'form-control'}),
            'Salary':forms.NumberInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'State':forms.Select(attrs={'class':'form-control'}),
            }




class Contactform(forms.ModelForm):
    Message=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Contact
        fields = ['Name','Mobile','State','Message']
        labels = {'Name':'FULL NAME','Mobile':'CONTACT NO','State':'STATE','Message':'MESSAGE'}
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'State':forms.Select(attrs={'class':'form-control'}),
            'Message':forms.Textarea(attrs={'cols':80,'rows':100}),
        }

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        labels = {'first_name': 'FIRST NAME', 'last_name': 'LAST NAME', 'email': 'EMAIL ID',
                  'username': 'USERNAME', 'password': 'PASSWORD'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
