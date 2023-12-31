"""
URL configuration for ShopDjango project.

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


from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from user import  views
from ShopDjango import settings
from posts.views import main_view, products_view, show_categories, products_detail_view ,product_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/create/', product_create_view),
    path('products/', products_view),
    path('products/<int:id>/', products_detail_view),
    path('categories/', show_categories),
    path('create/products/', product_create_view),
    path('user/register/', views.register_view),
    path('user/login/', views.login_view),
    path('user/logout/', views.logout_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


