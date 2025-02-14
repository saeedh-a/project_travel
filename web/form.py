from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import User

class TourPackageForm(forms.ModelForm):
   class Meta:
      model=   TourPackage
      fields= ['vendor','name','description','destination','price','duration','image','available','expiry_date','is_top_package','is_budget_friendly']

class VendorRegistrationForm(UserCreationForm):
   email  = forms.EmailField(required=True, help_text="enter a valid Email address")
   company_name = forms.CharField(max_length=100, required=True, help_text='Enter the name of your company.')
   contact_info =forms.CharField(widget=forms.Textarea, required=True, help_text='enter your contact information.')
   class Meta:
      model= User
      fields= ['username','email','password1','password2','company_name','contact_info']

class VendorLoginForm(AuthenticationForm):
     class Meta:
        fields=['username','password']


class UserRegistrationForm(UserCreationForm):
   email = forms.EmailField()
   class Meta:
      model = User
      fields= ['username','email','password1','password2']

class userLoginForm(AuthenticationForm):
     class Meta:
        model = User
        fields=['username','password']


class BookingForm(forms.ModelForm):
   class Meta:
      model = Booking
      fields= ['number_of_people',]


   
def __init__(self, *args,**kwargs):
  self.package= kwargs.pop('package', None)
  self.user= kwargs.pop('user', None)
  super().__init__(*args,**kwargs)

def save(self, commit=True):
   instance=super().save(commit=False)
   instance.package=self.package
   instance.user=self.user
   instance.total_price=self.package.price * instance.numbe_of_people
   if commit :
      instance.save()
      return instance
  