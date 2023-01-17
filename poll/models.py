from django.db import models

# Create your models here.


GENDER = {
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
}
COLORS = {
    (" ", "--SELECT--"),
    ("Red", "RED"),
    ("Green", "GREEN"),
    ("Pink", "PINK"),
    ("Black", "BLACK"),
}

class Student_register(models.Model):
    fname = models.CharField(max_length=30, verbose_name="First Name", help_text="first_name")
    lname = models.CharField(max_length=30, verbose_name="Last Name", help_text='last_name')
    email = models.EmailField(help_text="Email Id", error_messages="Enter Valid Email")
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER)
    colors = models.CharField(max_length=10, choices=COLORS)



# 37.9