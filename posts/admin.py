from django.contrib import admin

from posts.models import Product, Hashtag , Category

admin.site.register(Product)
admin.site.register(Hashtag)
admin.site.register(Category)
