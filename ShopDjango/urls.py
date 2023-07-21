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

from ShopDjango import settings
from posts.views import main_view, products_view, hashtags_view, show_categories, post_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),

    path('products/', products_view),
    path('products/<int:id>/', post_detail_view),

    path('hashtags/', hashtags_view),
    path('categories/', show_categories),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


