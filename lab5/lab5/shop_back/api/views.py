from django.shortcuts import render
from .models import Product, Category
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    data = list(products.values())
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    product = Product.objects.filter(id=id).values()
    return JsonResponse(list(product), safe=False)

def caregory_list(request):
    categories = Category.objects.all()
    data = list(categories.values())
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    category = Category.objects.filter(id=id).values()
    return JsonResponse(list(category), safe=False)

def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    data = list(products.values())
    return JsonResponse(data, safe=False)

