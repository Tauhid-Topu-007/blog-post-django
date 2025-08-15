from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<slug:slug>/', views.blogpost, name='blogpost'),
    
]
