from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('login', views.user_login, name="login"),
    # path('login', auth_views.auth_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('logout-then-login', auth_views.logout_then_login, name='logout_then_login'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='account/registration/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/registration/password_reset_done.html'), name='password_reset_done'),
    re_path('password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/',
            auth_views.PasswordResetConfirmView.as_view(template_name='account/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('register', views.register, name='register'),
    path('', views.dashboard, name='dashboard')
]
