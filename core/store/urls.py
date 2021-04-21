from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop-categoria/<slug:category_slug>/', views.category_list, name='category_list'),
    path('shop-subcategoria/<slug:subcategory_slug>/', views.subcategory_list, name='subcategory_list'),
]


