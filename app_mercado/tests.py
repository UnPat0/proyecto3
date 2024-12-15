from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Productos

class ProductosTestCase(TestCase):
    def setUp(self):
        # Crea datos de prueba
        Productos.objects.create(producto="Producto 1", precio=10.5, stock=50)
        Productos.objects.create(producto="Producto 2", precio=20.0, stock=30)

    def test_producto_nombre(self):
        """Los nombres de los productos deben ser correctos"""
        producto = Productos.objects.get(producto="Producto 1")
        self.assertEqual(producto.producto, "Producto 1")

    def test_producto_precio(self):
        """Los precios de los productos deben ser correctos"""
        producto = Productos.objects.get(producto="Producto 1")
        self.assertEqual(producto.precio, 10.5)

    def test_total(self):
        """El cálculo del total debe ser correcto"""
        producto = Productos.objects.get(producto="Producto 1")
        self.assertEqual(producto.total(), 10.5)
