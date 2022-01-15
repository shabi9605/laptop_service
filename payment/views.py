from django.contrib import messages
from django.db.models.fields import PositiveIntegerField
from .models import *
from django.shortcuts import render
import razorpay
from .forms import PaymentForm
from cart1.models import *
from orders.models import *
from account.models import *

def payment(request):
    
    t=request.user.cart.total_amount
    cart=Cart.objects.get(user=request.user)
    order=request.session['order']
    orders=Order.objects.get(id=order)
    print(orders.paid)
    

    if request.method == "POST":
        # name = request.POST.get('name')
        # amount1=request.POST.get('amount')
        amount = t *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        print(request.user.cart.total_amount)
        t=request.user.cart.total_amount
        
        if order_status == 'created':
            payment = Payment(
                amount=t,
                order_id=order_id,
                total_amount=t,
                user=request.user,
                
            )
          
        payment.save()
        
        
        response_payment['user'] = request.user
        cart=Cart.objects.get(user=request.user)
        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment.html', {'form':form,'payment': response_payment,'cart':cart})
    cart=Cart.objects.get(user=request.user)
    form = PaymentForm()
    return render(request, 'payment/payment.html', {'form': form,'amount':t,'cart':cart})







def payment2(request,invoice_id):
    
    
    invoice=Invoice.objects.get(id=invoice_id)
    print(invoice)
    t=invoice.booking.price
    print(t)
    request.session['invoice']=invoice.id

    if request.method == "POST":
        # name = request.POST.get('name')
        # amount1=request.POST.get('amount')
        amount = t *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=int(amount),
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        print(request.user.cart.total_amount)
        t=invoice.booking.price
        
        if order_status == 'created':
            payment = Payment(
                amount=t,
                order_id=order_id,
                total_amount=t,
                user=request.user,
                
            )
          
        payment.save()
        
        response_payment['user'] = request.user

        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment2.html', {'form':form,'payment': response_payment,'amount':t})

    form = PaymentForm()
    return render(request, 'payment/payment2.html', {'form': form,'amount':t})


    


    
    order=Order.objects.get(id=orders_id)
    print(order.price)
    t=order.price
    

    if request.method == "POST":
        # name = request.POST.get('name')
        # amount1=request.POST.get('amount')
        amount = t *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=int(amount),
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        print(request.user.cart.total_amount)
        t=order.price
        
        if order_status == 'created':
            payment = Payment(
                amount=t,
                order_id=order_id,
                total_amount=t,
                user=request.user,
                
            )
          
        payment.save()
        
        order=Order.objects.update_or_create(id=orders_id,
        defaults={'paid':'paid'}
        )
        response_payment['user'] = request.user

        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment2.html', {'form':form,'payment': response_payment})

    form = PaymentForm()
    return render(request, 'payment/payment2.html', {'form': form,'amount':t})



def payment_status(request):
    try:
        order=request.session['order']
        orders=Order.objects.get(id=order)
        print(orders.paid)
    except:
        pass
    response = request.POST
    params_dict = {

       'razorpay_order_id': response['razorpay_order_id'],
       'razorpay_payment_id': response['razorpay_payment_id'],
       'razorpay_signature': response['razorpay_signature'],
     
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
    

    try:
        status = client.utility.verify_payment_signature(params_dict)
        payment = Payment.objects.get(order_id=response['razorpay_order_id'])
        payment.payment_id = response['razorpay_payment_id']

        payment.is_paid = True
        payment.save()
        try:
            order=request.session['order']
            orders=Order.objects.get(id=order)
            print(orders.paid)
            requirement=Order.objects.update_or_create(id=order,
            defaults={'paid':True}
            )
            print(orders.paid)
        except:
            pass
        try:
            invoice=request.session['invoice']
            invoice=Invoice.objects.update_or_create(id=invoice,
            defaults={'status':True})
        except:
            pass
        return render(request, 'payment/payment_status.html', {'status': True,'payment_id':payment.payment_id})
    except:
        return render(request, 'payment/payment_status.html', {'status': False})


def allpayments(request):
    payall=Payment.objects.all()
    return render(request,'payment/allpayment.html',{'payall':payall})

def userpaymentview(request):
    userpay=Payment.objects.filter(user=request.user)
    return render(request,'payment/userpayment.html',{'userpay':userpay})