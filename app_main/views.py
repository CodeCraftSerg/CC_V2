import requests
import environ

from datetime import date
from django.shortcuts import render
from django.templatetags.static import static

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


def main(request):
    # API_WEATHER_KEY = env("API_WEATHER_KEY")
    # ABSTRACT_API_KEY = env("ABSTRACT_API_KEY")
    #
    # url_1 = (
    #     "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="
    #     + API_WEATHER_KEY
    # )
    #
    # response_ip = requests.get("https://api.ipify.org?format=json")
    # if response_ip.status_code == 200:
    #     public_ip = response_ip.json()["ip"]
    # else:
    #     public_ip = None
    # # print(public_ip)
    #
    # if public_ip:
    #     response_city = requests.get(
    #         "https://ipgeolocation.abstractapi.com/v1/?api_key="
    #         + ABSTRACT_API_KEY
    #         + "&ip_address="
    #         + public_ip
    #     )
    #     # print(response_ip.status_code)
    #     # print(response_ip.content)
    #     if response_city.status_code == 200:
    #         data = response_city.json()
    #         city_temp = data["city"]
    #         if city_temp:
    #             city = city_temp
    #         else:
    #             city = "Kyiv"
    #     else:
    #         city = "Kyiv"
    # else:
    #     city = "Kyiv"
    #
    # # city = "Kyiv"
    #
    # city_weather = requests.get(url_1.format(city)).json()
    #
    # weather = {
    #     "city": city,
    #     "temperature": city_weather["main"]["temp"],
    #     "description": city_weather["weather"][0]["description"],
    #     "icon": city_weather["weather"][0]["icon"],
    #     "temperature_max": city_weather["main"]["temp_max"],
    #     "temperature_min": city_weather["main"]["temp_min"],
    #     "feelslike_weather": city_weather["main"]["feels_like"],
    # }
    #
    # url_2 = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date.today().strftime('%d.%m.%Y')}"
    #
    # currency_exchange = requests.get(url_2).json()
    #
    # exchange_rates = {}
    # for item in currency_exchange["exchangeRate"]:
    #     currency = item["currency"]
    #     if currency in ["USD", "EUR"]:
    #         if date.today().strftime("%d.%m.%Y") not in exchange_rates:
    #             exchange_rates[date.today().strftime("%d.%m.%Y")] = {}
    #         exchange_rates[date.today().strftime("%d.%m.%Y")][currency] = {
    #             "sale": float(item["saleRate"]),
    #             "purchase": float(item["purchaseRate"]),
    #         }
    #
    # return render(
    #     request,
    #     "app_main/index.html",
    #     {"weather": weather, "exchange_rates": exchange_rates},
    # )
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
