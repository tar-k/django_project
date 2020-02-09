from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('news/', views.index, name='index'),
]