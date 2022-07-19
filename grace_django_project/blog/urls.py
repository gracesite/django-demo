from django.urls import path
from . import views

urlpatterns = [
    path('home/',  views.home,  name='blog-home'), # Home page
    path('about/', views.about, name='blog-about'), # About page
]