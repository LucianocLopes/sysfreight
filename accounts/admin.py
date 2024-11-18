from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts import forms, models


@admin.register(models.UserMain)
class UserMainAdmin(UserAdmin):
    add_form = forms.UserMainCreateForm
    form = forms.UserMainChangeForm
    model = models.UserMain
    list_display = ('first_name', 'last_name', 'email', 'cpf', 'is_staff')
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'cpf')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    ]


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    '''Admin View for models.UserProfile'''

    list_display = ('user', 'birth_date', 'gender')