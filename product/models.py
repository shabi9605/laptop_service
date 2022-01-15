from django.db import models
from datetime import datetime
from django.db.models.fields.files import ImageFileDescriptor
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,db_index=True)
    description=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

   
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image=models.ImageField(upload_to='product_image/%Y/%m/%d')
    price=models.PositiveIntegerField()
    
    price_declare_date=models.DateTimeField()
    stock=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('account:product_detail', args=[self.id, self.slug])


    