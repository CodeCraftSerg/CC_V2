import requests
import environ

from django.shortcuts import render
from django.templatetags.static import static

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


def main(request):
    logo_logo = static("app_main/images/logo/logo.svg")
    logo_white = static("app_main/images/logo/logo-white.svg")
    context = {"logo_logo": logo_logo, "logo_white": logo_white}
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
