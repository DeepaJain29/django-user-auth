from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import timedelta
from django.utils import timezone

# Extend the default User model to customize it
class User(AbstractUser):
    # Additional fields can be added here if needed
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')], default='user')
    # The password_hash and is_active are already handled by AbstractUser, so no need to redefine them

    def __str__(self):
        return self.username

# ActivationToken model for email verification
class ActivationToken(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f"Activation Token for {self.user.username}"

    def is_expired(self):
        return timezone.now() > self.expiration_date

# PasswordResetToken model for resetting passwords
class PasswordResetToken(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f"Password Reset Token for {self.user.username}"

    def is_expired(self):
        return timezone.now() > self.expiration_date