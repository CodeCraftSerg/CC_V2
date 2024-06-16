from django.core.validators import RegexValidator
from django.forms import (
    Form,
    CharField,
    TextInput,
    EmailField,
    EmailInput,
)

from .models import ContactUs


class ContactUsForm(Form):
    full_name = CharField(
        max_length=75,
        min_length=8,
        required=True,
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "fullName",
                "placeholder": "John Doe",
                "class": "w-full border-0 border-b border-[#f1f1f1] bg-transparent pb-3 text-body-color placeholder:text-body-color/60 focus:border-primary focus:outline-none dark:border-dark-3 dark:text-dark-6",
            }
        ),
    )
    email = EmailField(
        max_length=320,
        required=True,
        widget=EmailInput(
            attrs={
                "type": "email",
                "name": "email",
                "placeholder": "example@yourmail.com",
                "class": "w-full border-0 border-b border-[#f1f1f1] bg-transparent pb-3 text-body-color placeholder:text-body-color/60 focus:border-primary focus:outline-none dark:border-dark-3 dark:text-dark-6",
            }
        ),
    )
    phone = CharField(
        max_length=20,
        required=True,
        validators=[
            RegexValidator(
                regex=r"\+?\d{1,3}\(?\d{2,4}\)?\d{3}(?:-?\d{3,4})(\d{3})?",
                message="Phone number must be entered in the format: "
                "+CountryCode(operator code)phone number example: +380(50)1234567. Up to 15 digits allowed.",
            )
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "phone",
                "placeholder": "+380(50)1234567",
                "class": "w-full border-0 border-b border-[#f1f1f1] bg-transparent pb-3 text-body-color placeholder:text-body-color/60 focus:border-primary focus:outline-none dark:border-dark-3 dark:text-dark-6",
            }
        ),
    )
    message = CharField(
        max_length=500,
        min_length=6,
        required=True,
        widget=TextInput(
            attrs={
                "type": "message",
                "rows": "1",
                "placeholder": "type your message here",
                "class": "w-full resize-none border-0 border-b border-[#f1f1f1] bg-transparent pb-3 text-body-color placeholder:text-body-color/60 focus:border-primary focus:outline-none dark:border-dark-3 dark:text-dark-6",
            }
        ),
    )

    class Meta:
        model = ContactUs
        fields = "__all__"
