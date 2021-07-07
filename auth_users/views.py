from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request,'index.html')

# Login
def login_view(request):
    return render(request,'login.html')

# Registering User
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request,user)
            send_email(request)
            return redirect('/')
        
        context = {'form':form}
    else:       
        form = RegisterForm()
        context = {'form':form}
        return render(request,'registration/register.html',context)


# Send Email when User is registered.
def send_email(request):
    users = request.user
    print(users.email)
    send_mail(
    'Register Notification',
    'Hello, ' + request.user.username + ' Register is completed. Thank You.',
    'youremail@something.com',
    [users.email],
    fail_silently=False,
    )
    return HttpResponse("Email has been sent")