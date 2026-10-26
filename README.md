# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
'''
admin.py
from django.contrib import admin
from .models import Student,StudentAdmin
admin.site.register(Student,StudentAdmin)

models.py
from django.db import models
from django.contrib import admin
class Student(models.Model):
    Sno=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    Phone_No=models.IntegerField()
    Address=models.TextField()
    Depart=models.CharField(max_length=10)
    Ref_no=models.IntegerField()
    
    
class StudentAdmin(admin.ModelAdmin):
    list_display=["Sno","Name","Phone_No","Address","Depart","Ref_no"]
'''


## OUTPUT!:
[alt text](<Screenshot 2026-10-26 190743.png>)

Include the screenshot of your admin page.


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
