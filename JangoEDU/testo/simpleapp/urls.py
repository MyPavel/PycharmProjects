from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductsList.as_view(), name='product_list'),
    path('products/search/', ProductsSearch.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('products/create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('orders/', IndexView.as_view()),
    path('orders/new/', NewOrderView.as_view(), name = 'new_order'),
    path('orders/take/<int:oid>', take_order, name = 'take_order')
]
