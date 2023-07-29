from django import forms
from posts import models


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=5, max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    created_date = forms.DateTimeField()
    modified_date = forms.DateTimeField()
    category = forms.ModelChoiceField(queryset=models.Category.objects.all())


class CategoryCreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    icon = forms.ImageField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=255)
