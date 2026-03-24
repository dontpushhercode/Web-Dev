from django.shortcuts import render
from .models import Product, Category
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    data = list(products.values())
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        data = list(product.values())
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found!'}, status=404)

def category_list(request):
    categories = Category.objects.all()
    data = list(categories.values())
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        data = list(category.values())
        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found!'}, status=404)

def products_by_category(request, category_id):
    try:
        products = Product.objects.filter(category_id=category_id)
        data = list(products.values())
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Products not found!'}, status=404)

