from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import CoachRegistrationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'index.html')

def signin_user(request):
    return render(request,'registration/login.html')

def register(request):
    rgf = CoachRegistrationForm()
    if request.method == 'POST':
        rgf = CoachRegistrationForm(request.POST)
        if rgf.is_valid():
            print(rgf)
            rgf.save()
            user = rgf.cleaned_data.get('username')
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    
    return render(request, 'registration/signup.html', {'rgf': rgf})

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
            

    return render(request, 'registration/login.html')