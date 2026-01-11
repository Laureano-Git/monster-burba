from django.shortcuts import render
from rest_framework import viewsets
from .models import Hamburguesa
from .serializers import HamburguesaSerializer
from .models import InformacionNegocio
from .serializers import InformacionNegocioSerializer
from .models import OpcionesExtra
from .serializers import OpcionesExtraSerializer
from .models import Product
from .serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer

class HamburguesaViewSet(viewsets.ModelViewSet):
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer
# Create your views here.

class InformacionNegocioViewSet(viewsets.ModelViewSet):
    queryset = InformacionNegocio.objects.all()
    serializer_class = InformacionNegocioSerializer

class OpcionesExtraViewSet(viewsets.ModelViewSet):
    queryset = OpcionesExtra.objects.all()
    serializer_class = OpcionesExtraSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
