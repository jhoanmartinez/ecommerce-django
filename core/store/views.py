from django.shortcuts import render
import random
from .models import *

def homepage(request):
    products = Product.objects.all() #Grab the 20 mkost selled
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

# def all_products(request):
#     products = Product.objects.all()