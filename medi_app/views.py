from django.http import HttpResponse
from django.shortcuts import render
from .models import User, EmailVerification
from .services.email_service import send_verification_email


def verify_email(request, token):
    try:
        verification = EmailVerification.objects.get(token=token)
        user = verification.user
        user.is_email_verified = True
        user.save()
        return HttpResponse("Email verified successfully.")
    except EmailVerification.DoesNotExist:
        return HttpResponse("Invalid verification token.")
    
def save(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create(
        username=name,
        email=email,
        password=password
    )

    verification = EmailVerification.objects.create(
        user=user
    )
    # Send email here

    send_verification_email(user)
   
    return HttpResponse("Check your email for verification.")

def register(request):
    return render(request, 'register.html')
