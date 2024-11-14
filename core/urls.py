from django.urls import path, include

from core import views

app_name = 'core'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]