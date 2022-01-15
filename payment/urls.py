from django.urls import path
from .import views

app_name = 'payment'
urlpatterns = [
    path('payment',views.payment,name='payment'),
    path('payment2/<int:invoice_id>',views.payment2,name='payment2'),

    

    path('payment-status', views.payment_status, name='payment-status'),
    path('allpayment',views.allpayments,name='allpayment'),
    path('userpayment',views.userpaymentview,name='userpayment')


    
]
