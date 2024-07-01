from django.urls import path, include

from . import views

app_name = "app_news"

urlpatterns = [
    path("", views.main, name="news_main"),
    path("tech_news/", views.tech_news, name="tech_news"),
    path("sports_news/", views.sports_news, name="sports_news"),
    path("science_news/", views.science_news, name="science_news"),
    path("health_news/", views.health_news, name="health_news"),
    path("entertainment_news/", views.entertainment_news, name="entertainment_news"),
    path("business_news/", views.business_news, name="business_news"),
]
