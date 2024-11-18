from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts import models


class UserMainCreateForm(UserCreationForm):

    class Meta:
        model = models.UserMain
        fields = ('first_name', 'last_name', 'cpf')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class UserMainChangeForm(UserChangeForm):

    class Meta:
        model = models.UserMain
        fields = ('first_name', 'last_name', 'cpf')


class SignupForm(forms.Form):   
    username = forms.CharField(label = 'Usuário')
    password1 = forms.CharField(label = 'Senha', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirme', widget = forms.PasswordInput)


class LoginForm(forms.Form):   
    username = forms.CharField(label = 'Usuário')
    password = forms.CharField(label = 'Senha', widget = forms.PasswordInput)