from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import CoachRegistrationForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    rgf = CoachRegistrationForm()
    user = request.user
    if request.method == 'POST':
        rgf = CoachRegistrationForm(request.POST)
        if rgf.is_valid():
            print(rgf)
            # if rgf.cleaned_data.email == user.email:
            #       print('A user with this email already exists')
                  
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
        # print(username)
        password = request.POST.get('password')
        # print(password)

        user = authenticate(request, username = username, password = password)
        # print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
            

    return render(request, 'registration/login.html')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "email/password_reset_email.txt"
					c = {
					"email":user.email,
					"user":user.username,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request,'registration/password_reset.html', context={"password_reset_form":password_reset_form})

# def signin_user(request):
#     return render(request,'registration/login.html')


