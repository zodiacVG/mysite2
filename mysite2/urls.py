"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import view
urlpatterns = [
    url(r'^search-student$', view.show_student),
    url(r'^add-student$', view.addStudent),
    url(r'^modify-student/(?P<id>\d+)$', view.modifyStudent, name='modifyStudent'),
    url(r'^delete-student/(?P<id>\d+)$', view.deleteStudent, name='deleteStudent'),

    url(r'^search-instructor$', view.show_instructor),
    url(r'^add-instructor$', view.addInstructor),
    url(r'^modify-instructor/(?P<id>\d+)$', view.modifyInstructor, name='modifyInstructor'),
    url(r'^delete-instructor/(?P<id>\d+)$', view.deleteInstructor, name='deleteInstructor'),
]
