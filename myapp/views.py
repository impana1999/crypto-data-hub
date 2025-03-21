from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Organization, CryptoPrice
from .serializers import OrganizationSerializer, CryptoPriceSerializer
from .permissions import IsOrgCreator

class CryptoPricePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class OrganizationListCreateView(generics.ListCreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['created_at']
    search_fields = ['name']

    def get_queryset(self):
        return Organization.objects.filter(created_by=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class OrganizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrgCreator]

class CryptoPriceListCreateView(generics.ListCreateAPIView):
    serializer_class = CryptoPriceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CryptoPricePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['symbol', 'org']
    search_fields = ['symbol']

    def get_queryset(self):
        return CryptoPrice.objects.all().order_by('-timestamp')

class CryptoPriceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CryptoPrice.objects.all()
    serializer_class = CryptoPriceSerializer
    permission_classes = [permissions.IsAuthenticated]
