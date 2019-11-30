from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='workbench-home'),
    path('about/', views.about, name='workbench-home-about'),
]