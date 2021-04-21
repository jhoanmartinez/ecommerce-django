from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search-categories/<slug:category_slug>/', views.category_list, name='category_list'),
    path('search-subcategories/<slug:subcategory_slug>/', views.subcategory_list, name='subcategory_list'),
]


