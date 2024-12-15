from django.db import models

# Create your models here.

class Productos(models.Model):
    
    producto = models.CharField(max_length =  255, blank = True, null = True)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, null = True)
    stock = models.PositiveIntegerField(blank = True, null = True)
    cantidad_a_comprar = models.PositiveIntegerField(default = 1)

    
    def total(self):
        if self.precio and self.cantidad_a_comprar:
            
            return self.precio * self.cantidad_a_comprar
    
        else:
            0


    def __str__(self):
        return f"Producto: {self.producto}\n cantidad: {self.cantidad_a_comprar}\n Total: {self.total}"
    
    
class Clientes(models.Model):
    
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    direccion = models.CharField(max_length = 255)
    correo = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\n Dirección: {self.direccion}\n Correo: {self.correo}"
