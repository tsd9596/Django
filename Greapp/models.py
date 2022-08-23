from django.db import models
GENDER_CHOICE = (("Male","Male"),("Female","Female"))

STATE_CHOICE = (
("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),
("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),
("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),
("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),
("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


# Create your models here.

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(choices=GENDER_CHOICE, max_length=255, null=True, blank=True)
    DOB = models.DateTimeField()
    Age = models.IntegerField()
    Mobile = models.BigIntegerField()
    City = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Email = models.EmailField()
    State = models.CharField(choices=STATE_CHOICE, max_length=255, null=True, blank=True)


class Contact(models.Model):
    Name = models.CharField(max_length=255)
    Mobile = models.BigIntegerField()
    State = models.CharField(choices=STATE_CHOICE,max_length=255,null=True, blank=True)
    Message = models.CharField(max_length=255)