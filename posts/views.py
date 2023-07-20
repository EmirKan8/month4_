from django.shortcuts import render
from posts.models import Product, Hashtag, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context_data = {
            'posts': products
        }

        return render(request, 'products/products.html', context=context_data)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context_data = {
            'hashtags': hashtags
        }
        return render(request, 'hashtags/hashtags.html', context=context_data)


def show_categories(request):
    categories = Category.objects.all()

    contex_data = {
        'categories':categories
    }
    return render(request, 'categories/categories.html', context=contex_data)





