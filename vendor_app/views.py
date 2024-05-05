from math import ceil
from rest_framework import generics,permissions # type: ignore
from .models import Vendor, PurchaseOrder
from .serializers import *
from django.db.models import Avg,F
from django.utils import timezone
from django.http import JsonResponse
from .models import Vendor, PurchaseOrder
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta


class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    #permission_classes = [permissions.IsAuthenticated]


class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    #permission_classes = [permissions.IsAuthenticated]
    

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    #permission_classes = [permissions.IsAuthenticated]

def calculate_performance_metrics(vendor):
    # On-Time Delivery Rate
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_deliveries = completed_pos.filter(order_date__lt=F('delivery_date')).count()
    total_completed_pos = completed_pos.count()
    on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100 if total_completed_pos else 0

    # Quality Rating Average
    quality_rating_avg = completed_pos.aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0

    # Average Response Time
    response_times = completed_pos.annotate(response_time=F('acknowledgment_date') - F('issue_date'))
    average_response_time_timedelta = response_times.aggregate(avg_response=Avg('response_time'))['avg_response']
    # Convert timedelta to hours
    average_response_time = average_response_time_timedelta.total_seconds() / 3600 if average_response_time_timedelta else 0

    # Fulfilment Rate
    issued_pos = vendor.purchase_orders.count()
    fulfillment_rate = round((completed_pos.count() / issued_pos), 2) if issued_pos else 0

    # Create and save VendorPerformance instance
    performance = VendorPerformance.objects.create(
        vendor=vendor,
        date=timezone.now(),  # Assuming you want to save the metrics for the current date
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time,
        fulfillment_rate=fulfillment_rate
    )

    vendor_performance = Vendor.objects.get(name=vendor)
    vendor_performance.on_time_delivery_rate = on_time_delivery_rate
    vendor_performance.quality_rating_avg = quality_rating_avg
    vendor_performance.average_response_time =average_response_time
    vendor_performance.fulfillment_rate = fulfillment_rate
    vendor_performance.save()
    return {
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': average_response_time,
        'fulfillment_rate': fulfillment_rate
    }

def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
        performance_metrics = calculate_performance_metrics(vendor)
        return JsonResponse(performance_metrics, status=200)
    except Vendor.DoesNotExist:
        return JsonResponse({'error': 'Vendor not found'}, status=404)
    
@csrf_exempt
def acknowledge_purchase_order(request, po_id):
    try:
        po = PurchaseOrder.objects.get(pk=po_id)
        po.acknowledgment_date = timezone.now()
        po.save()
        vendor = po.vendor
        performance_metrics = calculate_performance_metrics(vendor)
        return JsonResponse(performance_metrics, status=200)
    except PurchaseOrder.DoesNotExist:
        return JsonResponse({'error': 'Purchase Order not found'}, status=404)
    
@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        # Recalculate and update performance metrics
        calculate_performance_metrics(vendor)
