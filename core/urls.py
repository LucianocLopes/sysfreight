from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]