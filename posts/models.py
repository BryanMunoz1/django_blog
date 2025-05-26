from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200, default="Sin título")
    descripcion = models.TextField(default="Sin descripción")
    logo = models.ImageField(upload_to='img/', blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['orden', 'fecha_creacion']
        verbose_name = "Card de Automóvil"
        verbose_name_plural = "Cards de Automóviles"
        
    def __str__(self):
        return self.titulo