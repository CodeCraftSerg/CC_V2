from django.urls import path

from . import views

app_name = "app_main"

urlpatterns = [
    path("", views.main, name="root"),  # app_main:root
    path("app_main/success/", views.main, name="success"),
    path("app_main/privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("app_main/terms_of_use/", views.terms_of_use, name="terms_of_use"),
    path(
        "app_main/delete_personal_data/",
        views.delete_personal_data,
        name="delete_personal_data",
    ),
]
