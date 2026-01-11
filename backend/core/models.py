from django.db import models

class Category(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True, null=True)

    class meta:
        verborse_name_plural = "Categories" #para llamarlo en el admin

    def __str__(self):
        return self.nombre

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(help_text="Ingredientes de la hamburguesa")
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='hamburguesas/', null=True, blank=True)   
    # Precios segun tamaño
    precio_simple = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_doble = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_triple = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Opciones de tamaño
    permite_simple = models.BooleanField(default=True)
    permite_doble = models.BooleanField(default=True)
    permite_triple = models.BooleanField(default=True)
    # Ingredientes incluidos (para que Svelte los transforme en lista)
    # Ej: "Tomate, Legucha, Cebolla Morada, etc"
    ingredientes_default = models.CharField(
        max_length=255,
        default="Tomate, Lechuga",
        help_text="Separados por coma"
    )
    papas_sason = models.BooleanField(default=True)
    # ❗¡FORAING KEY! (clave foranea)
    # Le decimos que cada hamburguesa debe estar relacionada con UNA categoria.
    categoria= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    # Nuevo campo para las ofertas
    es_oferta= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre if self.categoria else 'Sin categoria'})"
# Create your models here.

class InformacionNegocio(models.Model):
    zona_atencion = models.CharField(max_length=200, default="La Plata")
    telefono = models.CharField(max_length=20)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    horario_atencion = models.TextField(help_text="Ej: Lun-Vie 18hs a 23 hs")

    #Este truco asegura que solo haya 1 registro (no queremos 2 direcciones distintas)
    def save(self, *args, **kwargs):
        if not self.pk and InformacionNegocio.objects.exists():
            #Si ya existe uno, no dejamos crear otro, solo editar
            return
        return super(InformacionNegocio, self).save(*args, **kwargs)
    
    def __str__(self):
        return "Información del Negocio"
    
class OpcionesExtra(models.Model):
    nombre = models.CharField(max_length=100)
    # Ej: Aderezo, acompañamiento, tipo de pan, etc
    tipo = models.CharField(max_length=50,
                            help_text="Clasificación de la opción (ej: Aderezo, Extra, Pan)")
    precio_adicional= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.tipo} {self.nombre} (+${self.precio_adicional})]"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='extras/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Solo ingresar si tiene valor adicional")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    def __str__(self):
        return f"[{self.category}] {self.name}"