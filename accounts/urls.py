# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login_view, name='login'),      # Login page
    path('logout/', views.logout_view, name='logout'),   # Logout page
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),  # Password reset page
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),  # Password reset confirmation
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
