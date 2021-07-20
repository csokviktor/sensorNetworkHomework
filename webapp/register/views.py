from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def register(response):
    if response.user.is_authenticated:
        messages.warning(response, "You are already logged in!")
        return redirect('/')
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        messages.success(response, "You have registered successfully.")
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {"form": form})