from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(r'register', views.register, name='register'),
    path(r'login', views.loginPage, name='login'),
    path(r'logout', views.logoutUser, name='logout'),
]

urlpatterns += [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
