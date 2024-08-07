from django.contrib import admin
from .models import userdetail,clientdetail,parlour,service,servicemaster,Cart,booking,Payment

# Register your models here.

@admin.register(userdetail)
class userAdmin(admin.ModelAdmin):
    list_display=('id','username','name','mobile','email')

@admin.register(clientdetail)
class userAdmin(admin.ModelAdmin):
    list_display=('id','username','regno','parlourname','location')

@admin.register(parlour)
class userAdmin(admin.ModelAdmin):
    list_display=('id','parlour_name','address','rating','description','parlour_image')

@admin.register(servicemaster)
class userAdmin(admin.ModelAdmin):
    list_display=('id','service_name')

@admin.register(service)
class userAdmin(admin.ModelAdmin):
    list_display=('id','parlourname','servicename','images','description','charges','discounted_charges')

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=('id','user','service','quantity')

@admin.register(booking)
class CartModelAdmin(admin.ModelAdmin):
    list_display=('id','user','parlourname','service','quantity','booking_date','Time_slot','status')

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=('id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid')
