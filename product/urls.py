from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('category_list',views.category_list,name='category_list'),
    path('add_category',views.add_category,name='add_category'),
    path('product_create',views.product_create,name='product_create'),
    path('product_list1',views.product_list1,name='product_list1'),
    path('delete_product/<int:id>',views.delete_product,name ='delete_product'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('product',views.product,name='product'),
    path('categorysearch/<int:id>',views.categorysearch,name='categorysearch'),
    path('product_search', views.product_search, name='product_search'),
    path('product_detail<int:id>',views.product_detail, name='product_detail'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)