from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})


def graph(response):
    print(User().is_authenticated)
    if not response.user.is_authenticated:
        messages.warning(response, "Please Log in first")
        return redirect('/')
    return render(response, 'main/graph.html', {})