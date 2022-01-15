from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.auth.decorators import login_required


# Create your views here.


def category_list(request):
    list=Category.objects.all()
    return render(request,'product/category_view.html',{'list':list})


def add_category(request):
    if request.method=='POST':
        category_form=CategoryForm(request.POST,request.FILES)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,'Category add successfully')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        category_form=CategoryForm()
    return render(request,'product/add_category.html',{'category_form':category_form})



# create Product
def product_create(request):
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request,'Product add successfully')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        product_form=ProductForm()
    return render(request,'product/create_product.html',{'product_form':product_form})

def product_list1(request):
    list=Product.objects.all().order_by('-created')
    return render(request,'product/product_list.html',{'list':list})


def update_product(request,id):
    Update = Product.objects.get(id=id)
    print(Update)
    form= ProductForm(instance=Update)
    if request.method=='POST':
        form= ProductForm(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('product_list1')
    return render(request,'product/product_edit.html',{'form':form,'product':Update})

def delete_product(request,id):
    deleteemp = Product.objects.get(id=id)
    deleteemp.delete()
    messages.success(request,'Record deleted succefully')
    return redirect('product_list1')

#product deatils

def product(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

        products = products.filter(category=category)
    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(1)
    is_authenticated = request.user.is_authenticated
    print(is_authenticated)
    if is_authenticated:
        # wishlist = Wishlist.objects.filter(user=request.user)

        return render(
            request,
            'product/product.html',
            {
                'category': category,
                'categories': categories,
                'products': products,
                # 'wishlist': wishlist
            }
        )

    else:
        return render(
            request,
            'product/product.html',
            {
                'category': category,
                'categories': categories,
                'products': products,
            }
        )


def categorysearch(request,id):
    listing = get_object_or_404(Category, id=id)
    print(listing)
    product=Product.objects.order_by('-created').filter(category_id=listing.id)
    return render(request,'product/category.html',{'listings':product})


def product_search(request):
    results = None
    try:
        query = request.POST['query']
        results = Product.objects.filter(name__icontains=query) |\
            Product.objects.filter(description__icontains=query)
        page = request.GET.get('page')
        paginator = Paginator(results, 6)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(1)
        return render(
            request,
            'product/product.html',
            {'products': results}
        )
    except KeyError:
        wishlist = None
        "KeyError"
        return render(
            request,
            'product/product.html',
            {'products': results}
        )

def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id,
        is_available=True
    )

    return render(
        request,
        'product/detail.html',
        {'product': product}
    )




