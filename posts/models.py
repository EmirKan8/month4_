from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/')





class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None, null=True)

    def __str__(self):
        return f'{self.title}'

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title