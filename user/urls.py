from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('register-options/', registration_options, name='register-options'),
    path('email_verification/<str:uidb64>/<str:token>', email_verification, name='email-verification'),
    path('email_verification_sent/', email_verification_sent, name='email-verification-sent'),
    path('email_verification_success/', email_verification_success, name='email-verification-success'),
    path('email_verification_failed/', email_verification_failed, name='email-verification-failed'),

    path('login/', Login.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password/password-reset.html'), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/password/password-reset-sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password/password-reset-form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password/password-reset-complete.html'), name='password_reset_complete'),
    
]
