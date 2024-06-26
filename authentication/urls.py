"""
URL configuration for mainapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from . import views

app_name = "authentication"

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('sign_up_user/', views.sign_up_user, name='sign_up_user'),
    path('signup_page/', views.signup_view, name='signup_view'),
    path('log_in_user/', views.log_in_user, name='log_in_user'),
    path('logout/', views.logout_user, name='logout_user'),


]
