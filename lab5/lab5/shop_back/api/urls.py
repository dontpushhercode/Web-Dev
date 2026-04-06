from django.urls import path
from .views import  ProductListAPIView, ProductDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, CategoryProductsAPIView

#FBV, CBV:

# urlpatterns = [
#     path('products/', product_list, name='product_list'),
#     path('products/<int:product_id>/', product_detail, name='product_detail'),
# ]

#mixins:

# urlpatterns = [
#     path('products/', ProductListAPIView.as_view(), name='product_list'),
#     path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product_detail'),
# ]

#generics:

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view()),
]