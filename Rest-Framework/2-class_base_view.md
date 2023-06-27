from rest_framework.permissions import (
    IsAuthenticated,
    BasePermission,
    SAFE_METHODS
)
from .serializers import ProductSerializer
from products.models import Product



class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print(request.user, obj.user)
        if request.method in SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView, IsOwnerOrReadOnly):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView, IsOwnerOrReadOnly):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



