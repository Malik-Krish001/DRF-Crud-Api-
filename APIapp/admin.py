from django.contrib import admin
from APIapp.models import StudentModel
# Register your models here.

@admin.register(StudentModel)

class StudentModelAdmin(admin.ModelAdmin):
    list_display=["name","phone_no","dob","address","roll_no"]
