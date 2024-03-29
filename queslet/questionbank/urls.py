"""queslet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import home_view,mcq_view,search_view,import_view,manage_view,export_view,forbiden_view,edits_views

urlpatterns = [
    path('',home_view.home,name="home"),
    path('manage/',manage_view.manage,name="manage"),
    path('mcq/',mcq_view.mcq_view,name="mcq_view"),
    path('search/',search_view.search_view,name="search_view"),
    path('import/',import_view.import_view,name="import_view"),
    path('export/',export_view.export,name="export_view"),
    path('forbiden/',forbiden_view.forbiden,name="forbiden"),
    path('edit_mcq/',edits_views.edit_mcq,name='edit')

    # path('admin/', admin.site.urls,name="admin"),
]

