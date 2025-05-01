
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/products', views.ProductViewSet)
router.register(r'api/categories', views.CategoryViewSet)

app_name = 'products'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<str:category_name>/', views.category_detail, name='category_detail'),
    path('', include(router.urls)),
]
