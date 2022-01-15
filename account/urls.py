from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('dashboard',views.dashboard,name='dashboard'),

    path('send_complaint',views.send_complaint,name='send_complaint'),
    path('my_complint',views.my_complint,name='my_complint'),
    path('all_complaint',views.all_complaint,name='all_complaint'),
    
    path('add_rating',views.add_rating,name='add_rating'),

    path('book_service',views.book_service,name='book_service'),
    path('my_booking',views.my_booking,name='my_booking'),
    path('all_booking',views.all_booking,name='all_booking'),
    path('recieved_booking',views.recieved_booking,name='recieved_booking'),

    path('make_invoice',views.make_invoice,name='make_invoice'),
    path('invoices',views.invoices,name='invoices'),
    path('my_invoices',views.my_invoices,name='my_invoices'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)