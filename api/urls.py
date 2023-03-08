from django.urls import path
# Create your models here.
from .views import Products,Cakes,Materials,Desserts,InsumosView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('products',csrf_exempt(Products.as_view()), name="products"),
    path('material',csrf_exempt(Materials.as_view()), name="material"),
    path('insumos',csrf_exempt(InsumosView.as_view()), name="insumos"),
    path('desserts',csrf_exempt(Desserts.as_view()), name="desserts"),
    path('cakes',csrf_exempt(Cakes.as_view()), name="cakes"),
]