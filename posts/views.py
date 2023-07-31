from django.shortcuts import render, redirect

from posts.forms import ProductCreateForm , CategoryCreateForm,  ReviewCreateForm
from posts.models import Product, Category, Review


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

def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                quantity=form.cleaned_data.get('quantity'),
                image=form.cleaned_data.get('image')
            )
            return redirect('/products/')
        return render(request, 'products/create.html', context={
            'form': form
        })

def products_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context = {
            'product': product,
            'review': product.review_set.all(),
            'user': request.user
        }
        return render(request, 'products/detail.html', context=context)
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = request.POST
        form = ReviewCreateForm(data=data)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product

            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)


def show_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        contex_data = {
            'categories':categories
        }
        return render(request, 'categories/categories.html', context=contex_data)


def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():

            return redirect('product-list')
    else:
        form = ProductCreateForm()

    return render(request, 'products/create.html', {'form': form})
