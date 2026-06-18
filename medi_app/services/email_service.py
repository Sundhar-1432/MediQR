from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_verification_email(user):
    token = user.emailverification.token
    verification_link = (
        f"http://127.0.0.1:8000/verify/{token}/"
    )

    html_content = render_to_string(
        "emails/verify_email.html",
        {
            "user": user,
            "verification_link": verification_link
        }
    )

    email = EmailMultiAlternatives(
        subject="Verify Your MediQR Account",
        body="Verify your account",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )

    email.attach_alternative(
        html_content,
        "text/html"
    )

    email.send()