"""
URL configuration for shop project.

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
from django.contrib import admin
from django.urls import path
from shops.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_shop/',register_shop,name='register_shop'),
    
    path('shops/',shop_list,name='shop-list'),
    path('shops/search/',search_nearby_shops,name='search-shops'),
    path('search_shops/',search_shops,name='search_shops'),
    
    
    
]
