from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "cards"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cards ordenadas
        cards = Post.objects.all().order_by('orden', 'fecha_creacion')
        
        # Cambiar cards_data por additional_data para que coincida con el template
        context['additional_data'] = []
        for card in cards:
            context['additional_data'].append({
                'title': card.titulo,  # Cambiar titulo por title
                'description': card.descripcion,  # Cambiar descripcion por description
                'logo': card.logo.url if card.logo else '',
            })
        
        return context