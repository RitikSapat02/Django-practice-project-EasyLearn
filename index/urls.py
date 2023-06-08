from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('This-is-me-Ritik/',views.aboutus,name = 'about'),
]