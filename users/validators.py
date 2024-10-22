from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            f"The user with {value} already exists.", params={"value": value}
        )


def reset_email(value):
    if not User.objects.filter(email=value).exists():
        raise ValidationError(
            f"The user with {value} not registered.", params={"value": value}
        )
