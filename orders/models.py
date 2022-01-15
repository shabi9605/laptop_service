from django.db import models
from product.models import Product
from account.models import User
from payment.models import *

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20,null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True) 
    state = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    complete=models.BooleanField(default=False)
    packed='packed'
    shipped='shipped'
    delivered='delivered'
    statuses=[
        (packed,'packed'),
        (shipped,'shipped'),
        (delivered,'delivered')
    ]
    paid = models.BooleanField(default=False)

    status=models.CharField(max_length=30,choices=statuses,default=packed)
    

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {} {}'.format(self.user, self.id,self.user)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    order = models.ForeignKey(Order,
    related_name='order_items',
    on_delete=models.CASCADE,
    )
    product = models.ForeignKey(Product,
    related_name='order_products',
    on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity