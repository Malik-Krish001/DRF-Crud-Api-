from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50,verbose_name="Name")
    phone_no=models.BigIntegerField(verbose_name="Phone No.")
    dob=models.DateField(verbose_name="Date of birth")
    address=models.TextField(verbose_name="Address")
    roll_no=models.IntegerField(verbose_name="Roll No.")

    class Meta:
        db_table="Student_dtl"

    
    def __str__(self):
        return self.name
    
    
