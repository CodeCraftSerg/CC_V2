import environ
import logging

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.template.loader import render_to_string

from .forms import ContactUsForm

logger = logging.getLogger(__name__)

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


def main(request):
    logo_logo = static("app_main/images/logo/logo.svg")
    logo_white = static("app_main/images/logo/logo-white.svg")

    if request.method == "POST":
        logger.debug("Received POST request")
        form = ContactUsForm(request.POST)
        if form.is_valid():
            logger.debug("Form is valid")
            full_name = form.cleaned_data.get("full_name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            message = form.cleaned_data.get("message")

            html_letter = render_to_string(
                "app_main/contact_us_letter.html",
                {
                    "name": full_name,
                    "email": email,
                    "phone": phone,
                    "message": message,
                },
            )

            logger.debug(
                f"Sending mail to: {env('RECIPIENT_1')} and {env('RECIPIENT_2')}, from: {settings.EMAIL_HOST_USER}"
            )

            send_mail(
                subject="Received contact form submission",
                message="This is message",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[env("RECIPIENT_1"), env("RECIPIENT_2")],
                html_message=html_letter,
            )
            return render(request, "app_main/success.html")
        else:
            logger.debug("Form is not valid")
            logger.debug(form.errors)
    else:
        logger.debug("Received GET request")
        form = ContactUsForm()

    context = {
        "logo_logo": logo_logo,
        "logo_white": logo_white,
        "form": form,
    }
    return render(request, "app_main/index.html", context)


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", context={})


def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", context={})


def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", context={})


def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", context={})


def privacy_policy(request):
    return render(request, "app_main/privacy_policy.html", context={})


def terms_of_use(request):
    return render(request, "app_main/terms_of_use.html", context={})


def delete_personal_data(request):
    return render(request, "app_main/delete_personal_data.html", context={})
