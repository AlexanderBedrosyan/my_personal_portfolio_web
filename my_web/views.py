from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .models import ContactMessage
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'base.html')


def certificates(request):
    return render(request, 'certificates.html')


def contacts(request):
    return render(request, 'contacts.html')


def projects(request):
    return render(request, 'projects.html')


def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        messages.success(request, ('Your message has been sent successfully.'))
        return redirect('home')
    messages.success(request, ('Method not allowed.'))
    return redirect('home')