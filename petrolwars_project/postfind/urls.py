from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='postfind-home'),
    path('share/', views.share, name='postfind-share'),
    path('search/', views.search, name='postfind-search'),
]