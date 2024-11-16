from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model  # Use get_user_model()

# Get the custom User model
User = get_user_model()

# Registration form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # This will use the custom User model
        fields = ['username', 'email', 'password1', 'password2']

# Login form
class LoginForm(AuthenticationForm):
    pass
