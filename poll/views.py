from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import Register
from .models import Student_register

# Create your views here.
# Model  API (36)

def Home(request):
    if request.method == "POST":
        fm = Register(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['fname']
            lname = fm.cleaned_data['lname']
            em = fm.cleaned_data['email']
            pw1 = fm.cleaned_data['password1']
            pw2 = fm.cleaned_data['password2']
            gen = fm.cleaned_data['gender']
            col = fm.cleaned_data['colors']
            data = Student_register(fname=fname, lname=lname, email=em, password1=pw1, password2=pw2, gender=gen, colors=col)
            data.save()
            return HttpResponseRedirect('/thank/')
    else:
        fm = Register()  
    return render (request, 'home.html', {'form':fm})


def thank(request):
    return render(request, 'thanks.html')