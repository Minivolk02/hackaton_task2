from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import *
from .forms import *
from .views import user_logout, user_register

urlpatterns = [
    path('login/', LoginView.as_view(form_class=UserAuthenticationForm, template_name='users/login.html', redirect_authenticated_user=True),
         name='user_login'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='user_logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html',
                                                      html_email_template_name='users/template_letter/password_reset_email.html', form_class=UserPasswordResetForm),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html', ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             form_class=UserSetPasswordForm,
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html',
         ),
         name='password_reset_complete'),
    path('password-change/', PasswordChangeView.as_view(template_name='users/password-change.html', form_class=UserPasswordChangeForm),
         name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password-change-done.html'),
         name='password_change_done'),
]
