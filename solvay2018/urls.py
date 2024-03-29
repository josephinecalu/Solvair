"""solvay2018 URL Configuration

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
from django.contrib import admin
from solvay2018.views import *
from django.conf.urls import url

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    url(r'^logout',logout,name='logout'),
    url(r'^login',login,name='login'),
    url(r'^home',home,name='home'),
    url(r'^sign-up',signup,name='signup'),
    url(r'^delete',delete,name='delete'),
    url(r'^reservation',reservation,name='reservation'),
    url(r'^demo',demo,name='demo')
]
