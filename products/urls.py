from django.urls import path
from .views import products, product

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('product/<int:pk>/', product, name='detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]