from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from .models import MailSettings
# Create your views here.
from emailmanager.mail_create import send


def login(request):
    print("come to login func")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        return render(request, 'registration/login.html')


@login_required(login_url='login')
def home(request):
    is_check = MailSettings.objects.all()
    print(is_check, request.user)

    if request.method == "POST":
        receiver = request.POST["receiver_mail"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        date = request.POST["date"]
        send(receiver, subject, message, date)
        return render(request, 'homepage.html', {'mail': request.user.email})
    return render(request, 'homepage.html', {'mail': request.user.email})
