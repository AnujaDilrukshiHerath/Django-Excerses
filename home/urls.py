from django.urls import path
from .views import (
    FunnelStatusListCreateView, FunnelStatusRetrieveUpdateDestroyView,
    CustomerListCreateView, CustomerRetrieveUpdateDestroyView,
    CustomerLogListCreateView, CustomerLogListPaginationView,
)

urlpatterns = [
    path('funnel-status/', FunnelStatusListCreateView.as_view(), name='funnel-status-listCreate'),
    path('funnel-status/<int:pk>/', FunnelStatusRetrieveUpdateDestroyView.as_view(), name='funnel-status-detail'),
    path('customer/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('customer-log/', CustomerLogListCreateView.as_view(), name='customer-log-list'),
    path('customer-log/paginated/', CustomerLogListPaginationView.as_view(), name='customer-log-paginated'),
]
