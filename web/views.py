from django.shortcuts import render

from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .form import *
from django.contrib.auth import  login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm


# Create your views here.
def home(request): 
    packages= TourPackage.objects.all()
    return render(request,'home.html',{"packages":packages})

def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(data=request.POST)
        if form.is_valid():
         form.save()
        return redirect("vendor_login")
    else:
        form =VendorRegistrationForm()
    return render(request,'vendor_register.html',{"form":form})
    

def vendor_login(request):
    if request.method=="POST":
        form=VendorLoginForm(data= request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
            return redirect('vendor_dashboard')
    else:
        form =VendorLoginForm()
    return render(request,'vendor_login.html',{'form':form})


def add_packages(request):
    if request.method =="POST":
        form= TourPackageForm(request.POST,request.FILES)
        if form.is_valid():
          form.save()    
        return redirect('vendor_dashboard')
    else:
        form = TourPackageForm()
    return render(request,'add_packages.html',{'form':form})
    

def edit_package(request,pk): 
    vendor = get_object_or_404(Vendor, user=request.user)
    package = get_object_or_404(TourPackage ,pk= pk, vendor=vendor)
    if request.method =="POST":
        form = TourPackageForm(request.POST,request.FILES, instance=package)
        if form.is_valid():
            form.save()
        return redirect("vendor_dashboard")
    else:
         form=TourPackageForm(instance=package)
    return render(request, "edit_package.html",{"form":form})
        

def delete_package(request,pk):
    package= get_object_or_404(TourPackage, pk=pk,vendor_user=request.user)
    if request.method =='POST':
      package.delete()
    return redirect("vendor_dashboard")


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST )
        if form.is_valid():
            user= form.save()
            login(request,user)
        return redirect ('user_login')
    else:
        form= UserRegistrationForm()
    return render (request,'register.html',{'form':form})
    

def  user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST )
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
             login(request,user)
        return redirect('home')
    else:
        form= userLoginForm()
    return render(request,'login.html',{'form':form})
    
def vendor_logout(request):
    logout(request)
    return redirect('vendor_login')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

@login_required(login_url='user_login')
def book_package(request,pk):
    package=get_object_or_404(TourPackage,pk=pk)
    if request.method =='POST':
        form =BookingForm(request.POST)
        if form.is_valid():
         form.save()

        return redirect('payment_view',pk=pk)
    else:
      form=  BookingForm(initial={'package':package})
    return render(request,'booking.html',{'form':form, 'package':package})



def payment_view(request,pk):
    booking =get_object_or_404(Booking, pk=pk)
    package=booking.package
    return render(request, 'payment.html',{'booking':booking ,'package':package,})


@login_required 
def vendor_dashboard(request):
    packages =TourPackage.objects.all()
    return render(request,'vendor_dashboard.html',{'packages':packages})



def package_list(request):
   packages= TourPackage.objects.all()
   return render(request,'package_list.html',{'packages':packages})

def package_details(request,pk):
    package=get_object_or_404(TourPackage,pk=pk)
    return render(request,'package_details.html',{'package':package})

def admin_dashboard(request):
    vendors=Vendor.objects.all()
    packages=TourPackage.objects.all()
    context={'vendors':vendors,'packages':packages,'approved_packages':packages.filter(approved=True),'pending_packages':packages.filter(approved=False),}
    return render (request, 'admin_dashboard',context)

def approve_package(request,package_id):
    package = get_object_or_404(package,id=package_id)
    package.approved =True
    package.save()
    return redirect('admin_dashboard')

def reject_package(request,package_id):
    package = get_object_or_404(package,id=package_id)
    package.approved =False
    package.save()
    return redirect('admin_dashboard')

def browse_packages(request):
    all_packages=TourPackage.objects.all()
    top_packages=TourPackage.objects.filter(is_top_package=True) 
    budget_friendly=TourPackage.objects.filter(is_budget_friendly=True) 
    return render(request,'browse_packages.html',{'all_packages':all_packages,'top_packages':top_packages,'budget_friendly':budget_friendly})
    

def my_bookings(request):
    if request.user.is_authenticated:
     bookings =Booking.objects.filter(user =request.user)
     return render(request,'my_bookings.html',{'bookings':bookings})
    else:
        return('You need to log in to access this page.')














