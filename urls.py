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
    path('admin_change_password', views.admin_change_password, name='admin_change_password'),
    path('admin_logout', views.admin_logout, name='admin_logout'),

    path('admin_view_users', views.admin_view_users, name='admin_view_users'),
    path('admin_view_company', views.admin_view_company, name='admin_view_company'),

    path('admin_add_category', views.admin_add_category, name='admin_add_category'),
    path('admin_view_category', views.admin_view_category, name='admin_view_category'),
    path('admin_delete_category', views.admin_delete_category, name='admin_delete_category'),

    path('admin_add_sub_category', views.admin_add_sub_category, name='admin_add_sub_category'),
    path('admin_view_sub_category', views.admin_view_sub_category, name='admin_view_sub_category'),
    path('admin_delete_sub_category', views.admin_delete_sub_category, name='admin_delete_sub_category'),

    path('admin_add_dataset', views.admin_add_dataset, name='admin_add_dataset'),
    path('admin_view_dataset', views.admin_view_dataset, name='admin_view_dataset'),
    path('admin_delete_dataset', views.admin_delete_dataset, name='admin_delete_dataset'),

    path('admin_view_app', views.admin_view_app, name='admin_view_app'),

    path('company_login', views.company_login, name='company_login'),
    path('company_home', views.company_home, name='company_home'),
    path('company_change_password', views.company_change_password, name='company_change_password'),
    path('company_logout', views.company_logout, name='company_logout'),
    path('company_registration', views.company_registration, name='company_registration'),

    path('company_add_app', views.company_add_app, name='company_add_app'),
    path('company_view_app', views.company_view_app, name='company_view_app'),
    path('company_delete_app', views.company_delete_app, name='company_delete_app'),

    path('user_login', views.user_login2, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('user_registration', views.user_registration, name='user_registration'),
    path('user_change_password', views.user_change_password, name='user_change_password'),
    path('user_logout', views.user_logout, name='user_logout'),

    path('user_view_company', views.user_view_company, name='user_view_company'),
    path('user_view_app', views.user_view_app, name='user_view_app'),

]