from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Student(models.Model):
    depts = [
        ('civil', 'Civil Engineering'),
        ('cse', 'Computer Science and Engineering'),
        ('ece', 'Electronics and Communication Engineering'),
        ('eee', 'Electrical and Electronics Engineering'),
        ('eie', 'Electrical and Instrumentation Engineering'),
        ('ibt', 'Industrial Biotech Engineering'),
        ('it', 'Information Technology'),
        ('mech', 'Mechanical Engineering'),
        ('prod', 'Production Engineering')
    ]
    year = [
        ('one', "First"),
        ('two', "Second"),
        ('three', "Third"),
        ('four', "Final")
    ]
    name = models.CharField(max_length = 255)
    reg_no = models.CharField(max_length = 9)
    department = models.CharField(max_length = 6, choices = depts)
    phone_No = PhoneNumberField()
    year_Of_Study = models.CharField(max_length=5, choices = year)
    date_Added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reg_no

    
class MarksheetData(models.Model):
    '''
    To Store Information of the marksheet. Has - Register Number(Foreign Key from "Student") and serial Number of the Marksheet.
    '''
    semester = [
        ('one', 'One'),
        ('two', 'Two'),
        ('three', 'Three'),
        ('four', 'Four'),
        ('five', 'Five'),
        ('six', 'Six'),
        ('seven', 'Seven'),
        ('eight', 'Eight'),
    ]
    reg_No = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    serial = models.CharField(max_length=6, blank=True)
    sem = models.CharField(max_length = 6, choices=semester)

    def __str__(self):
        return self.serial
    
    class Meta:
        verbose_name = 'Mark Sheet Info'
        verbose_name_plural = 'Mark Sheet Information'

class ImageData(models.Model):
    depts = [
        ('civil', 'Civil Engineering'),
        ('cse', 'Computer Science and Engineering'),
        ('ece', 'Electronics and Communication Engineering'),
        ('eee', 'Electrical and Electronics Engineering'),
        ('eie', 'Electrical and Instrumentation Engineering'),
        ('ibt', 'Industrial Biotech Engineering'),
        ('it', 'Information Technology'),
        ('mech', 'Mechanical Engineering'),
        ('prod', 'Production Engineering')
    ]
    image = models.ImageField()
    department = models.CharField(max_length = 6, choices = depts)
    register_number = models.ForeignKey(to=Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Image Data"
