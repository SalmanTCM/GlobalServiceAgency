from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Add more URL patterns for other views as needed
]
