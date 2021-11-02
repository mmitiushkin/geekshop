from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from products.models import Product, ProductCategory


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = "products"
    paginate_by = 3

    # Этот метод работает, но не одновременно с пагинацией
    # def get_queryset(self):
    #     category_id = self.kwargs['category_id']
    #     print(category_id)
    #     if category_id:
    #         return Product.objects.filter(category=category_id)


    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context


# def products(request, category_id=None, page=1):
#     context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     paginator = Paginator(products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, 'products/products.html', context)






