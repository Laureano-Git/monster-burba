from rest_framework import serializers
import os
from dotenv import load_dotenv
from .models import Hamburguesa
from .models import InformacionNegocio
from .models import OpcionesExtra
from .models import Product
from .models import Category

load_dotenv() #Carga las variables del archivo .env

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
# Y podrías usarlo en tus vistas para el teléfono

class HamburguesaSerializer(serializers.ModelSerializer):
    # Usamos SerializerMethodField para hacer la lógica manualmente
    categoria_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Hamburguesa
        fields = '__all__'

    def get_categoria_nombre(self, obj):
        #Lógica: si la hamburguesa tiene una categoria, devuelve el nombre. Si no, devuelve None o 'General'
        if obj.category:
            return obj.category.nombre
        return 'General'
class InformacionNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionNegocio
        fields = '__all__'

class OpcionesExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model=OpcionesExtra
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'


