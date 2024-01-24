from .models import Product, Order
from rest_framework import generics
from .serializer import ProductSerializer, OrderSerializer
from .permissions import CanPostProductPermission
from .permissions import CanPostProductPermission


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CanPostProductPermission]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name',]


class ProductRetrieveView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()




class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



