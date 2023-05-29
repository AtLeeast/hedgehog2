from django.shortcuts import render
from .models import AccountModel
from loguru import logger

from .utils.get_user_data import get_user_data


def index(request):
    return render(request, 'ecosite/index.html', get_user_data(request))


def about(request):
    return render(request, 'ecosite/about.html', get_user_data(request))


def registration(request):
    return render(request, 'ecosite/registration.html')


def login(request):
    return render(request, 'ecosite/login.html')


def statistics(request):
    return render(request, 'ecosite/statistics.html', get_user_data(request))

def profile(request):
    return render(request, 'ecosite/profile.html', get_user_data(request))


def quit(request):
    if "account_id" in request.session:
        email = AccountModel.objects.filter(id=request.session["account_id"])[0].email
        logger.info(f"User {email} terminated session on their account")

        del request.session["account_id"]

    return render(request, 'ecosite/login.html')
