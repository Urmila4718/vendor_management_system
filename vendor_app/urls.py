from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorListCreate.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
    path('purchase_orders/', views.PurchaseOrderListCreate.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('vendors/<int:vendor_id>/performance/', views.vendor_performance, name='vendor_performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', views.acknowledge_purchase_order, name='acknowledge_purchase_order'),
    path('purchase_orders/<int:pk>/acknowledge/', views.acknowledge_purchase_order, name='acknowledge_purchase_order'),

]
