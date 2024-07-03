from django.forms import ModelForm, FileField, FileInput, CharField, TextInput

from .models import UserFile


class UploadFileForm(ModelForm):
    filepath = FileField(
        widget=FileInput(
            attrs={
                "placeholder": "Choose a file",
                "class": "w-full px-5 py-3 text-base text-white transition duration-300 ease-in-out border rounded-md cursor-pointer border-primary bg-primary hover:bg-blue-dark",
            }
        )
    )
    file_description = CharField(
        max_length=255,
        required=False,
        widget=TextInput(
            attrs={
                "placeholder": "Enter a description for your file",
                "class": "w-full px-5 py-3 text-base transition bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 placeholder:text-dark-6 focus:border-primary dark:focus:border-primary focus-visible:shadow-none",
            }
        ),
    )

    class Meta:
        model = UserFile
        fields = ["filepath", "file_description"]
        exclude = ["user"]
