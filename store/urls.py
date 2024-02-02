from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns += [
    path(r'login', views.login, name='login'),
    path(r'register', views.register, name='register'),
]

urlpatterns += [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
