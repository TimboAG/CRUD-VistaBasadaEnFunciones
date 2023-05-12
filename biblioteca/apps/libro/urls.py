from django.urls import path
from .views import crear_autor



urlpatterns = [
    path('crear_autor/', crear_autor, name='crear_autor')
]
