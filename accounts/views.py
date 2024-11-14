from django.shortcuts import render
from django.views import View
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


class LoginView(PageTitleViewMixin, View):
    title = "Login"
    
    def get(self, request):
        data = { 'form': forms.LoginForm(),
                'title': "LOGIN",
            }
        return render(request, 'registration/login.html', data)

    def post(self, request):
        form = forms.LoginForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password \
                and authenticate(username=username, password=password):
                login(request, user)
                return HttpResponseRedirect(reverse(self.get_success_url))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }     
        return render(request, 'registration/login.html', data)

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse(self.get_success_url))
    
    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to