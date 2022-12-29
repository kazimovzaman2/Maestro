from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin

from .models import Product
from .serializers import ProductSerializer



"""       Generic view       """

# List and Create View page
class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
    
    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)

product_list_create_view = ProductListCreateAPIView.as_view()


# Detail view page
class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

product_detail_view = ProductDetailAPIView.as_view()


# Update view page
class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

    # def perform_update(self, serializer):
    #     return super().perform_update(serializer)

product_update_view = ProductUpdateAPIView.as_view()



# Destroy view page
class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     """
#     Bunu istifade etmiyeciyik
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()































"""       Mixin View       """




class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):    # HTTP -> GET
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):    # HTTP -> POST
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()
























"""      Function based view       """

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
