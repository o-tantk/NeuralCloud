from django.urls import path
from django_distill import distill_path

from . import views

app_name = 'algorithm'
urlpatterns = [
    distill_path('', views.IndexView.as_view(), name='index'),
]