"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('about/',views.about),
    path('show',views.show),
    re_path('^$',views.index),
    re_path(r'demo/(?P<year>\d{4})/(?P<mon>\d+)/(?P<day>\d+)',views.demo),
    path('gethtml/',views.gethtml),
    path('indextmp',views.indextmp),
    path('abc/',views.abc),
    path('abcd/',views.abcd),
    re_path('yufa/(\d+)/',views.yufa),
    path('staticdemo/',views.staticdemo)
]
