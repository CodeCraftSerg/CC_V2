from django.core.validators import RegexValidator
from django.forms import (
    ModelForm,
    CharField,
    TextInput,
    DateInput,
    BooleanField,
    CheckboxInput,
    DateField,
    EmailField,
)

from app_contacts.models import Contact, Address


class ContactForm(ModelForm):
    name = CharField(
        min_length=3,
        max_length=20,
        required=True,
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "name",
                "placeholder": "John*",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    surname = CharField(
        min_length=3,
        max_length=20,
        required=False,
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "surname",
                "placeholder": "Doe",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    email = EmailField(
        required=False,
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "email",
                "placeholder": "contact@mail.com",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    mobile_phone = CharField(
        required=False,
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
                "name": "mobile_phone",
                "placeholder": "+380(XX)XXXXXXX",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    work_phone = CharField(
        required=False,
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
                "name": "work_phone",
                "placeholder": "+380(XX)XXXXXXX",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    home_phone = CharField(
        required=False,
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
                "name": "home_phone",
                "placeholder": "+380(XX)XXXXXXX",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    birthdate = DateField(
        required=False, input_formats=["%d/%m/%Y"], widget=DateInput(format="%d/%m/%Y")
    )
    facebook = CharField(
        required=False,
        validators=[
            RegexValidator(
                regex=r"^https?://(www\.)?facebook\.com/.+",
                message="Enter a valid Facebook URL.",
            )
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "facebook",
                "placeholder": "https://facebook.com/",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    instagram = CharField(
        required=False,
        validators=[
            RegexValidator(
                regex=r"^https?://(www\.)?instagram\.com/.+",
                message="Enter a valid Instagram URL.",
            )
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "instagram",
                "placeholder": "https://instagram.com/",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    tiktok = CharField(
        required=False,
        validators=[
            RegexValidator(
                regex=r"^https?://(www\.)?tiktok\.com/.+",
                message="Enter a valid Tiktok URL.",
            )
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "tiktok",
                "placeholder": "https://tiktok.com/",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    is_favorite = BooleanField(
        required=False,
        label="Is favorite",
        widget=CheckboxInput(
            attrs={"placeholder": "is_favorite", "class": "form-check-input"}
        ),
    )

    class Meta:
        model = Contact
        fields = [
            "name",
            "surname",
            "email",
            "mobile_phone",
            "work_phone",
            "home_phone",
            "birthdate",
            "is_favorite",
            "facebook",
            "instagram",
            "tiktok",
        ]
        widgets = {
            "birthdate": DateInput(attrs={"type": "date"}),
        }


class AddressForm(ModelForm):
    country = CharField(
        required=False,
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "country",
                "placeholder": "Ukraine",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    city = CharField(
        required=False,
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "city",
                "placeholder": "Kyiv",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )
    address = CharField(
        required=False,
        widget=TextInput(
            attrs={
                "type": "text",
                "name": "address",
                "placeholder": "Maidan Nezalezhnosti",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )

    class Meta:
        model = Address
        fields = ["country", "city", "address"]
