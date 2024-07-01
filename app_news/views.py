import requests
import environ

from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

NEWSAPI_KEY = env("NEWSAPI_KEY")


@login_required
def main(request):
    return render(request, "app_news/news_main.html")


def date_time_conversion(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = dt.strftime("%b %d, %Y %H:%M")
    return formatted_date


def news(request, response_url):
    request_url = response_url
    news_request = requests.get(request_url).json()
    news_data = news_request["articles"]
    news_title = []
    news_description = []
    news_img = []
    news_url = []
    news_time = []

    for items in range(len(news_data)):
        src = news_data[items]
        news_title.append(src["title"])
        news_description.append(src["description"])
        news_img.append(src["urlToImage"])
        news_url.append(src["url"])
        news_time.append(date_time_conversion(src["publishedAt"]))

    news_list = list(zip(news_title, news_description, news_img, news_url, news_time))

    paginator = Paginator(news_list, 6)
    page_number = request.GET.get("page")
    try:
        news_on_page = paginator.page(page_number)
    except PageNotAnInteger:
        news_on_page = paginator.page(1)
    except EmptyPage:
        news_on_page = paginator.page(paginator.num_pages)

    context = {"news_list": news_on_page, "page_range": paginator.page_range}

    return context


@login_required
def tech_news(request):
    context = news(
        request,
        f"https://newsapi.org/v2/top-headlines?country=ua&category=technology&apiKey={NEWSAPI_KEY}",
    )
    return render(request, "app_news/tech_news.html", context)


@login_required
def sports_news(request):
    context = news(
        request,
        f"https://newsapi.org/v2/top-headlines?country=ua&category=sports&apiKey={NEWSAPI_KEY}",
    )
    return render(request, "app_news/sports_news.html", context)


@login_required
def science_news(request):
    context = news(
        request,
        f"https://newsapi.org/v2/top-headlines?country=ua&category=science&apiKey={NEWSAPI_KEY}",
    )
    return render(request, "app_news/science_news.html", context)


@login_required
def health_news(request):
    context = news(
        request,
        f"https://newsapi.org/v2/top-headlines?country=ua&category=health&apiKey={NEWSAPI_KEY}",
    )
    return render(request, "app_news/health_news.html", context)


@login_required
def entertainment_news(request):
    context = news(
        request,
        f"https://newsapi.org/v2/top-headlines?country=ua&category=entertainment&apiKey={NEWSAPI_KEY}",
    )
    return render(request, "app_news/entertainment_news.html", context)


@login_required
def business_news(request):
    context = news(
        request,
        f"https://newsapi.org/v2/top-headlines?country=ua&category=business&apiKey={NEWSAPI_KEY}",
    )
    return render(request, "app_news/business_news.html", context)
