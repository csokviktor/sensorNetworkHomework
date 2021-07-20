from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class LoginFormView(SuccessMessageMixin, LoginView):
    success_url = '/'
    success_message = "You were successfully logged in."


urlpatterns = [
    path('login/',
        LoginFormView.as_view(redirect_authenticated_user=True),
        name='login'
        )
]
