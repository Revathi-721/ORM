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