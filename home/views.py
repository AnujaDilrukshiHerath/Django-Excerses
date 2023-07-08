from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics
from .models import FunnelStatus, Customer, CustomerLog
from .serializers import FunnelStatusSerializer, CustomerSerializer, CustomerLogSerializer


class FunnelStatusListCreateView(generics.ListCreateAPIView):
    queryset = FunnelStatus.objects.all()
    serializer_class = FunnelStatusSerializer


class FunnelStatusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FunnelStatus.objects.all()
    serializer_class = FunnelStatusSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerLogListCreateView(generics.ListCreateAPIView):
    queryset = CustomerLog.objects.all().order_by('-updated_at')
    serializer_class = CustomerLogSerializer


class CustomerLogListPaginationView(generics.ListAPIView):
    queryset = CustomerLog.objects.all().order_by('-updated_at')
    serializer_class = CustomerLogSerializer
    pagination_class = LimitOffsetPagination

