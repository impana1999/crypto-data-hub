from django.urls import path
from .views import (
    OrganizationListCreateView, OrganizationRetrieveUpdateDestroyView,
    CryptoPriceListCreateView, CryptoPriceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('organizations/', OrganizationListCreateView.as_view(), name='org-list'),
    path('organizations/<uuid:pk>/', OrganizationRetrieveUpdateDestroyView.as_view(), name='org-detail'),
    path('crypto-prices/', CryptoPriceListCreateView.as_view(), name='crypto-list'),
    path('crypto-prices/<int:pk>/', CryptoPriceRetrieveUpdateDestroyView.as_view(), name='crypto-detail'),
]
