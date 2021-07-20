from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from . import views


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'register/login.html'
    success_url = '/'
    success_message = "You were successfully logged in."


urlpatterns = [
    path('', views.home, name='home'),
    path('graph/', views.graph, name='graph'),
    path('login/', LoginFormView.as_view(redirect_authenticated_user=True), name='login'),
]
