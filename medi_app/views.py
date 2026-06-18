from django.http import HttpResponse
from django.shortcuts import render


def save(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    print(name)

    return HttpResponse("Data saved successfully!")
def register(request):
    return render(request, 'register.html')
