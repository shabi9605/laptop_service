from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request,'index.html')


def register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         profile_form=ProfileForm()
    return render(request,'register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form}) 
     


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        
        return render(request,'login.html')




def dashboard(request):
    try:
        profile=Register.objects.get(user=request.user)
        return render(request,'dashboard.html',{'profile':profile})
    except:
        return render(request,'dashboard.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')



def send_complaint(request):
    if request.method=="POST":
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
            cp=Complaint(user=request.user,content=complaint_form.cleaned_data['content'])
            cp.save()
            return redirect('my_complint')
        else:
            return HttpResponse("Invalid form")
    complaint_form=ComplaintForm()
    return render(request,'complaint.html',{'form':complaint_form})



def my_complint(request):
    complaints=Complaint.objects.filter(user=request.user).order_by('-date')
    return render(request,'view_complaints.html',{'complaints':complaints})


def all_complaint(request):
    all_complaint=Complaint.objects.all().order_by('-date')
    return render(request,'view_complaints.html',{'complaints':all_complaint})


def add_rating(request):
    ratings=Rating.objects.all()
    if request.method=="POST":
        rating_form=RatingForm(request.POST)
        if rating_form.is_valid():
            cp=Rating(user=request.user,rating=rating_form.cleaned_data['rating'])
            cp.save()
            return redirect('add_rating')
        else:
            return HttpResponse("Invalid form")
    rating_form=RatingForm()
    return render(request,'rating.html',{'form':rating_form,'ratings':ratings})



def book_service(request):
    if request.method=="POST":
        service_booking_form=ServiceBookingForm(request.POST)
        if service_booking_form.is_valid():
            cp=BookService(user=request.user,complaint=service_booking_form.cleaned_data['complaint'],wanted_date=service_booking_form.cleaned_data['wanted_date'],country=service_booking_form.cleaned_data['country'],state=service_booking_form.cleaned_data['state'],district=service_booking_form.cleaned_data['district'],city=service_booking_form.cleaned_data['city'],pin=service_booking_form.cleaned_data['pin'])
            cp.save()
            return redirect('my_booking')
        else:
            return HttpResponse("Invalid form")
    service_booking_form=ServiceBookingForm()
    return render(request,'add_service_booking.html',{'form':service_booking_form})


def my_booking(request):
    my_booking=BookService.objects.filter(user=request.user)
    return render(request,'booking.html',{'booking':my_booking})


def all_booking(request):
    all_booking=BookService.objects.all()
    return render(request,'booking.html',{'booking':all_booking})



def make_invoice(request):
    completed_booking=BookService.objects.filter(complete=True)
    print(completed_booking)
    if request.method=="POST":
        invoice_form=CustomForm(request.POST)
        if invoice_form.is_valid():
            cp=Invoice(booking=invoice_form.cleaned_data['booking'])
            cp.save()
            return redirect('invoices')
        else:
            return HttpResponse("Invalid form")
    invoice_form=CustomForm()
    return render(request,'make_invoice.html',{'form':invoice_form})


def invoices(request):
    all_invoices=Invoice.objects.all()
    return render(request,'view_invoices.html',{'invoices':all_invoices})


def my_invoices(request):
    my_invoice=Invoice.objects.filter(booking__user=request.user)
    return render(request,'my_invoices.html',{'my_invoice':my_invoice})




def recieved_booking(request):
    received_booking=BookService.objects.filter(received=True)
    return render(request,'booking.html',{'booking':received_booking})
