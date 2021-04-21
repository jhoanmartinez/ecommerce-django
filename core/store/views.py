from django.shortcuts import render
import random
from .models import *
from django.shortcuts import get_object_or_404

def homepage(request):
    products = Product.objects.all()
    context = { 'products':products,
                'top_20_best_seller':products,}
    return render(request, 'homepage/homepage.html', context)

def categories(request):
    return{
        'categories':Category.objects.all()
    }

def subcategories(request):
    return{
        'subcategories':SubCategory.objects.all()
    }

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {'product': product}
    return render (request,"product/detail.html", context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = { 'category': category,
                'products': products,}
    return render(request, "product/category.html", context)

def subcategory_list(request, subcategory_slug):
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    products = Product.objects.filter(subcategory=subcategory)
    context = { 'subcategory': subcategory,
                'products': products,}
    return render(request, "product/subcategory.html", context)
