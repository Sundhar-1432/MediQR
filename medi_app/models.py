from django.db import models
import uuid

class User(models.Model):
    username = models.CharField(max_length=100)
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class EmailVerification(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)