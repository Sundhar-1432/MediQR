from django.http import HttpResponse
from django.shortcuts import render
from .models import User

def save(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    User.objects.create(username=name, email=email, password=password)
    
    return HttpResponse("Data saved successfully!")
def register(request):
    return render(request, 'register.html')
