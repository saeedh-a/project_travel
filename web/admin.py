from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import*

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display=('company_name', 'username')


class TourpackageAdmin(admin.ModelAdmin):
    list_display =('name','price','approved','destination','is_top_package','is_budget_friendly',) 
    search_field=('name','destination','price')
    list_filter =('approved','destination','is_top_package','is_budget_friendly')



admin.site.register(TourPackage,TourpackageAdmin)

admin.site.register(Vendor,VendorAdmin)

admin.site.register(Booking)

admin.site.register(payment)

