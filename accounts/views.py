from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create user
            login(request, user)  # Log the user in automatically after registration
            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            # messages.error(request, 'There was an error with your registration. Please try again.')
            # print(form.errors)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"There was an error with your registration: {error}")  # Show specific error for each field
            print(form.errors)  # Debugging form errors (check your console)
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            messages.success(request, 'Logged in successfully!')
            return redirect('home')  # Redirect to home or dashboard page
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# User logout view
def logout_view(request):
    messages.get_messages(request).used = True  # This ensures old messages are cleared
    logout(request)  # Log the user out
    messages.success(request, 'Logged out successfully!')
    return redirect('login')  # Redirect to the login page

# Password reset view
class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    def form_valid(self, form):
        print("Password reset email form is valid.")
        return super().form_valid(form)


# Password reset done view
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

def home(request):
    return render(request, 'home.html') 