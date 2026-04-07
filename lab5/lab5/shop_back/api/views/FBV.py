from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product
from api.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all() # all objects of product class
        serializer = ProductSerializer(products, many=True) # to_dict(), many - [{},{},{}]
        return Response(serializer.data) # return to_dict().to_json()
    
    elif request.method=='POST':
        serializer = ProductSerializer(data=request.data) # to_json().to_dict()
        if serializer.is_valid(): 
            serializer.save() # save if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT', 'DELETE'])
def product_detail(request, product_id):
    # firstly try to get product
    try:
        product = Product.objects.get(pk=product_id) # get provides only one object
    except Product.DoesNotExist as e:
        return Response({'error':str(e)}, status=status.HTTP_404_NOT_FOUND) # if such product doesn't exist
    
    if request.method == 'GET':
        serializer = ProductSerializer(product) # to_dict()
        return Response(serializer.data) # return to_dict().to_json()
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data) # to_dict().to_json(), replace product with request.data
        if serializer.is_valid():
            serializer.save() # save if valid
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
