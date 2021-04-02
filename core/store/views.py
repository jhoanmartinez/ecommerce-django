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
    return render (request,"product/detail.html")
