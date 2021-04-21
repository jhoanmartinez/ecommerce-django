from .models import Category, SubCategory

def categories(request):
    return{
        'categories':Category.objects.all()
    }

def subcategories(request):
    return{
        'subcategories':SubCategory.objects.all()
    }