from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'orden', 'fecha_creacion']
    list_editable = ['orden']
    search_fields = ['titulo', 'descripcion']
    
    fields = ('titulo', 'descripcion', 'logo', 'orden')