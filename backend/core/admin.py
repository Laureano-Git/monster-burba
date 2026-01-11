from django.contrib import admin
from .models import Hamburguesa
from .models import InformacionNegocio
from .models import Category
from .models import OpcionesExtra
from .models import Category
from .models import Product

admin.site.register(Hamburguesa)
# Register your models here.


admin.site.register(InformacionNegocio)

admin.site.register(Category)

admin.site.register(Category)

admin.site.register(OpcionesExtra)

admin.site.register(Product)
