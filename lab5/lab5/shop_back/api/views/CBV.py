from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from api.models import Product
from api.serializers import ProductSerializer

class ProductListAPIView(APIView):

    def get(self, request):
        products = Product.objects.all() # all products
        serializer = ProductSerializer(products, many=True) # to_dict()
        return Response(serializer.data) # to_dict().to_json()
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data) # to_json().to_dict()
        if serializer.is_valid():
            serializer.save() # save if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):

    def get_object(self, product_id): # reuse func to get product
        try:
            product = Product.objects.get(pk=product_id) # get product by id
            return product
        except Product.DoesNotExist as e:
            raise Http404
        
    def get(self, request, product_id):
        product = self.get_object(product_id) # get product
        serializer = ProductSerializer(product) # to_dict()
        return Response(serializer.data) # to_dict().to_json()
    
    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTEXN)