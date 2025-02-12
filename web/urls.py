from django.urls import path
from.import views as v

urlpatterns=[
    path('', v.home, name='home'),
    path('home/', v.home, name='home'),
    path('about/', v.about, name='about'),
    path('book/<int:pk>/', v.book_package, name='book_package'),
    path('package_list/', v.package_list, name='package_list'),
    path('user_login', v. user_login, name='user_login'),
    path('user_register/', v.user_register, name='user_register'),
    path('contact/',v.contact, name='contact'),
    path('vendor_dashboard/', v.vendor_dashboard, name='vendor_dashboard'),
    path('add_packages/',v.add_packages, name='add_packages'),
    path('vendor_register/',v.vendor_register, name='vendor_register'),
    path('vendor_logout/', v.vendor_logout, name='vendor_logout'),
    path('edit/<int:pk>/', v.edit_package, name='edit_package'),
    path('delete/<int:pk>/', v.delete_package, name='delete_package'),
    path('vendor_login/', v.vendor_login, name='vendor_login'),
    path('payment/<int:pk>/', v.payment_view, name='payment_view'),
    path('package_details/<int:pk>/', v.package_details, name='package_details'),
    path('admin/dashboard/', v.admin_dashboard, name='admin_dashboard'),
    path('admin/package/approve/<int:package_id>/', v.approve_package, name='approve_package'),
    path('admin/package/reject/<int:package_id>/', v.reject_package, name='reject_package'),
    path('package_list/browse_packages/', v.browse_packages,name ='brows_packages'),
    path('my_bookings/', v.my_bookings, name='my_bookings'),
     path('browse_packages/', v.browse_packages,name ='brows_packages'),
    
 ]
