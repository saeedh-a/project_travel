
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TourPackage(models.Model):
    name= models.CharField(max_length=255 ,default=0 )
    description= models.TextField(default=0)
    destination= models.CharField(max_length=255, default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2 ,default=0)    
    duration= models.CharField (max_length=50 , default=0) 
    image= models.ImageField(upload_to='gallary', default=0) 
    approved=models.BooleanField(default=False, null=True  )
    is_top_package =models.BooleanField(default=False)
    is_budget_friendly =models.BooleanField(default=False)
    available =models.BooleanField(default=True)
    expiry_date =models.DateField(help_text='Last date This package is available',null=True,blank=True, default=None)

class Booking(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    package= models.ForeignKey(TourPackage ,on_delete=models.CASCADE, null=True )
    booking_date= models.DateField(auto_now_add=True)
    number_of_people= models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10,decimal_places=2,null=True )    



class Vendor(models.Model):
      id=models.AutoField(primary_key=True, default=0)
      username= models.CharField(max_length=100,default=0 )
      company_name= models.CharField(max_length=100, default=0)
      email = models.EmailField(max_length=100 ,default=0)    
      contact_info = models.TextField(max_length=100 , default=0)    

   

class payment(models.Model):
    Booking= models.OneToOneField(Booking,on_delete=models.CASCADE ,default=0)
    amount= models.DecimalField(max_digits=10,decimal_places=2, default=0)
    payment_date= models.DateTimeField(auto_now_add=True )
    status= models.CharField( max_length=50 ,choices=[('success','success'),('failed','failed')],default='success')




