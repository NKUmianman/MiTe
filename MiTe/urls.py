"""
URL configuration for MiTe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from app01.views.admin import admin_home,admin_self,admin_sales,admin_user,admin_login
from app01.views import login,home,user,explore

urlpatterns = [
    # path('admin/', admin.site.urls),


    path('login/',login.login),
    path('home/',home.home),
    path('login/check/',login.login_check),
    path('user/', user.user),
    path('explore/', explore.explore),
    path('explore/detail/', explore.explore_detial),


    path('admin/login/', admin_login.login),
    path('admin/logout/', admin_login.logout),

    path('admin/home/', admin_home.home),

    path('admin/sales/', admin_sales.sales_list),
    path('admin/sales/add/', admin_sales.sales_add),
    path('admin/sales/delete/',admin_sales.sales_delete),
    path('admin/sales/detail/',admin_sales.sales_detail),
    path('admin/sales/edit/',admin_sales.sales_edit),

    path('admin/user/', admin_user.user_list),
    path('admin/user/add/',admin_user.user_add),
    path('admin/user/register/',admin_user.user_register),
    path('admin/user/delete/',admin_user.user_delete),
    path('admin/user/detail/',admin_user.user_detail),
    path('admin/user/edit/',admin_user.user_edit),

    path('admin/self/',admin_self.admin_list),
]
