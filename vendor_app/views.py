from rest_framework import generics,permissions # type: ignore
from .models import Vendor, PurchaseOrder
from .serializers import *
from django.db.models import Avg,F
from django.utils import timezone
from django.http import JsonResponse
from .models import Vendor, PurchaseOrder
from django.views.decorators.csrf import csrf_exempt

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
    completed_pos = vendor.purchase_orders.filter(status='Completed')
    on_time_deliveries = completed_pos.filter(order_date__lt=F('delivery_date')).count()
    total_completed_pos = completed_pos.count()
    on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100 if total_completed_pos else 0

    # Quality Rating Average
    quality_rating_avg = completed_pos.aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0

    # Average Response Time
    response_times = completed_pos.annotate(response_time=F('issue_date') - F('acknowledgment_date'))
    
    average_response_time = response_times.aggregate(avg_response=Avg('response_time'))['avg_response']
    
    # Fulfilment Rate
    successful_pos = completed_pos.filter(status='Completed')
    issued_pos = vendor.purchase_orders.count()
    fulfillment_rate = round((successful_pos.count() / issued_pos),2) 

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
