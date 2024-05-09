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
from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [

    path('login/', include('authentication.urls')),

    path('', views.blog_posts_list_view, name='blog_view'),
    path('post/<int:pk>/', views.blog_post_view, name='blog_post_view'),
    path('create_post_view/', views.create_post_view, name='create_post_view'),
    path('publish_post/', views.publish_post, name='publish_post'),
    path('delete_post/', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>/', views.edit_post_view, name='edit_post'),
    path('projects', views.projects_list_view, name='projects_list_view'),
    path('create_project_view/', views.create_project_view, name='create_project_view'),
    path('publish_project/', views.publish_project, name='publish_project'),
    path('project/<int:pk>/', views.project_view, name='project_view'),
    path('delete_project/', views.delete_project, name='delete_project'),
    path('edit_project/<int:pk>/', views.edit_project_view, name='edit_project'),
    path('about_me', views.about_me_view, name='about_me_view'),
]
