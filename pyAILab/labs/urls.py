"""pyAILab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # Home with list of labs
    url(r'^$', views.home, name=u"labs"),
    url(r'^home$', views.home, name=u"labs"),
    # Main page of a lab
    url(r'^(?P<slug>[\w-]+)$', views.view_lab_main, name=u"lab"),
    # Main page of an experience
    url(r'^(?P<lab_slug>[\w-]+)/(?P<xp_slug>[\w-]+)$', views.view_xp_main, name=u"xp")
]
