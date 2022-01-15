from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description','slug']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name','slug','image','price','stock','description','is_available','created']
    list_display_links = ['category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)