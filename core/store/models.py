from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(null=True, blank=True,max_length=255, db_index=True)
    slug = models.SlugField(null=True, blank=True,max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(null=True, blank=True,max_length=255, db_index=True)
    slug = models.SlugField(null=True, blank=True,max_length=255, unique=True)
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'subcategories'

    def get_absolute_url(self):
        return reverse('store:sub_category_list', args=[self.slug])

    def __str__(self):
        return str(self.name)



class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, blank=True,  on_delete=models.SET_NULL, related_name='product_creator')
    title = models.CharField(null=True, blank=True,max_length=255)
    author = models.CharField(null=True, blank=True,max_length=255, default='admin')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=False, blank=False,upload_to='images/', default='default.jpg')
    image_2 = models.ImageField(null=True, blank=True,upload_to='images/')
    image_3 = models.ImageField(null=True, blank=True,upload_to='images/')
    image_4 = models.ImageField(null=True, blank=True,upload_to='images/')
    slug = models.SlugField(null=True, blank=True,max_length=255)
    price = models.IntegerField(null=True, blank=True)
    sale_price = models.IntegerField(null=True, blank=True)
    disccount_percentage = models.IntegerField(null=True, blank=True)
    in_stock = models.BooleanField(null=True, blank=True,default=True)
    is_active = models.BooleanField(null=True, blank=True,default=True)
    sales = models.IntegerField(null=True, blank=True, default=0)
    rating = models.FloatField(null=True, blank=True, default=4.5)
    created = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True,auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    @property
    def price_less_disscount(self):
        return (self.price*self.disccount_percentage) // 100

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
