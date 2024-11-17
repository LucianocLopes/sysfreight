from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts import forms


user = get_user_model()

class PageTitleViewMixin:
    title = ""

    def get_title(self):
        """
        Return the class title attr by default,
        but you can override this method to further customize
        """
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class LoginView(PageTitleViewMixin, LoginView):
    template_name = "registration/login.html"
    title = 'Login'
    

class LogoutView(PageTitleViewMixin, TemplateView):
    template_name = 'registration/logout.html'
    title = 'Logout'
    
    def post(self, request):
        logout(request)
        return redirect('/')
