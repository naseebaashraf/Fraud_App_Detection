"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_change_password',views.admin_change_password,name='admin_change_password'),
    path('admin_logout',views.admin_logout,name='admin_logout'),


    path('admin_add_category',views.admin_add_category,name='admin_add_category'),
    path('admin_view_category',views.admin_view_category,name='admin_view_category'),
    path('admin_delete_category',views.admin_delete_category,name='admin_delete_category'),
    path('admin_add_dataset',views.admin_add_dataset,name='admin_add_dataset'),

    path('company_login', views.company_login, name='company_login'),
    path('company_home', views.company_home, name='company_home'),
    path('company_change_password',views.company_change_password,name='company_change_password'),
    path('company_logout',views.company_logout,name='company_logout'),
    

]