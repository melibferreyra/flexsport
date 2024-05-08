from django.db import models
import datetime

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploads/liga/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre   
    
class Equipo(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploads/equipo/', null=True, blank=True)

    def __str__(self):
        return self.nombre  
    
class Jugadores(models.Model):
    nombre= models.CharField(max_length=100)
    imagen= models.ImageField(upload_to='uploads/jugadores/', null=True, blank=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    liga= models.ForeignKey(Liga, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    contraseña =  models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first.nombre} {self.last_nombre}'
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(default=0, decimal_places=2, max_digits=9)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250, default='', blank=True, null=True )
    imagen = models.ImageField(upload_to='uploads/producto/')
    promocion= models.BooleanField(default=False)
    precio_promocion= models.DecimalField(default=0, decimal_places=2, max_digits=9)
    
    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    direccion = models.CharField(max_length=100, default='', blank=True)
    telefono = models.CharField(max_length=20, default='', blank=True)
    fecha = models.DateField(default=datetime.datetime.today)
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.producto