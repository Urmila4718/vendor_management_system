from django.contrib import admin
from .models import *


# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display =['name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

admin.site.register(Vendor,VendorAdmin)

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display =['vendor','po_number','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date']

admin.site.register(PurchaseOrder,PurchaseOrderAdmin)

class VendorPerformanceAdmin(admin.ModelAdmin):
    list_display =['vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

admin.site.register(VendorPerformance,VendorPerformanceAdmin)