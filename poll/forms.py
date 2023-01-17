from django import forms 
from django.core import validators
from .models import Student_register

# class Register(forms.Form):
#     fname = forms.CharField(label="First Name", 
#                             validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(6)])
#     lname = forms.CharField(label="Last Name",
#                             validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(6)])
#     email = forms.EmailField(label="Email Adress")
#     password1 = forms.CharField(label="Password", validators=[validators.MinLengthValidator(5)])
#     password2 = forms.CharField(label=" Confirm Password", validators=[validators.MinLengthValidator(5)])
#     gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER))
#     colors = forms.CharField(widget=forms.SelectMultiple(choices=COLORS))


# Model form

class Register(forms.ModelForm):
    password1 = None
    class Meta:
        model = Student_register
        fields = "__all__"
        # fields = ['fname','lname']
        # exclude = ['lname']
        
        labels = {
            'fname': "User First Name",
            'lname': "User Last Name",
            'email': "User Email Adress",
        }
        
        error_messages = {
            'fname' : {"required" : "User First Name Is Required"},
            'lname' : {"required" : "User Last Name Is Required"},
            'email' : {"required" : "User Email Is Required"},
            'password1' : {"required" : "User Password Required"},
            'password2' : {"required" : "Confirm Password Required"},
        }
        
        help_texts = {
            'fname': "User First Name",
            'lname': "User Last Name",
            'email': "User Email Adress",
        }
        
        widgets = {
            "email" : forms.EmailInput(),
            "password1" : forms.PasswordInput(),
            "password2" : forms.PasswordInput(),
        }
