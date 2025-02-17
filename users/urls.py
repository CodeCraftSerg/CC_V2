from django.urls import path, include
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)

from . import views
from .forms import LoginForm, UserPasswordResetForm, UserPasswordResetConfirm

app_name = "users"

urlpatterns = [
    path(
        "signup/",
        views.RegisterView.as_view(),
        name="signup",
    ),
    path(
        "signin/",
        LoginView.as_view(template_name="users/signin.html", form_class=LoginForm),
        name="signin",
    ),
    path(
        "signout/",
        LogoutView.as_view(template_name="users/signout.html"),
        name="signout",
    ),
    path(
        "reset-password/",
        views.ResetPasswordView.as_view(
            template_name="users/password_reset.html", form_class=UserPasswordResetForm
        ),
        name="password_reset",
    ),
    path(
        "reset-password/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset-password/confirm/<uidb64>/<token>/",
        views.UserPasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            form_class=UserPasswordResetConfirm,
            success_url="/users/reset-password/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset-password/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
