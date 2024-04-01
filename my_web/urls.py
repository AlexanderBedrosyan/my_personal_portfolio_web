from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('certificates/', views.certificates, name='certificates'),
    path('contacts-info/', views.contacts, name='contacts'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.send_message, name='send_message')
]