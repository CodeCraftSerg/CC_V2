from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.forms import CharField, TextInput, EmailField, EmailInput, PasswordInput
from users.validators import validate_email, reset_email


class RegisterForm(UserCreationForm):
    username = CharField(
        max_length=50,
        min_length=3,
        required=True,
        widget=TextInput(
            attrs={
                "placeholder": "Username",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    email = EmailField(
        max_length=320,
        validators=[validate_email],
        required=True,
        widget=EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    password1 = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    password2 = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "placeholder": "Confirm password",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = CharField(
        max_length=50,
        min_length=3,
        required=True,
        widget=TextInput(
            attrs={
                "placeholder": "Username",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password")


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = EmailField(
        max_length=320,
        validators=[reset_email],
        widget=EmailInput(
            attrs={
                "placeholder": "user@email.com",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
                "type": "email",
                "name": "email",
            }
        ),
    )


class UserPasswordResetConfirm(SetPasswordForm):

    new_password1 = CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    new_password2 = CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Confirm password",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
