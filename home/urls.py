"""accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from . import views

#TODO check how to add hashtag to views.index page
#check how to change class from active when clicking on the button

urlpatterns = [
    path('', views.index, name='home_index'),
    path('intro_post/', views.intro_post, name='intro_post'),
    path('abtest_post/', views.abtest_post, name='abtest_post'),
    path('blog/', views.blog, name='show-blog'),
    path('post/', views.post, name = 'post_single')
]