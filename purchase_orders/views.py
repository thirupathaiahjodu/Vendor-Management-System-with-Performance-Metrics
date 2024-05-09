from django.shortcuts import render

# Create your views here.
# purchase_orders/views.py
from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PurchaseOrder

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = 'purchase_orders_list.html'
    context_object_name = 'purchase_orders'

class PurchaseOrderDetailView(DetailView):
    model = PurchaseOrder
    template_name = 'purchase_order_detail.html'
    context_object_name = 'purchase_order'
