from django.contrib.auth import logout


def logout_when_refresh(request):
    logout(request)
