from django.dispatch import receiver
from django.shortcuts import render

# Create your views here.
from emailmanager.mail_create import send

def login(request):
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/register.html')


def home(request):
    
    if request.method == "POST":
        receiver=request.POST["receiver_mail"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        date=request.POST["date"]
        send(receiver,subject,message,date)
    return render(request, 'homepage.html')

