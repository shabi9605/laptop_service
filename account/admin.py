from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Register)
admin.site.register(Complaint)
admin.site.register(Rating)
admin.site.register(BookService)
admin.site.register(Invoice)