
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    category = request.GET.get('category', '')
    if category:
        products = products.filter(category=category)
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category,
        'search_query': search_query,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category_name)
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
