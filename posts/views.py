from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "post_list"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        additional_data = [
            {
                "title": "BUGATTI CHIRON SUPER SPORT 300+",
                "description": "El primer automóvil de producción en romper la barrera de los 300 mph (483 km/h), con un motor W16 de 8.0 litros que produce 1.578 CV y una velocidad máxima limitada de 440 km/h.",
                "logo": 'img/bugatti.jpg'
            },
            {
                "title": "PAGANI HUAYRA BC",
                "description": "Obra maestra del arte automotriz italiano con un motor V12 biturbo de 6.0 litros desarrollado por AMG que genera 791 CV, con carrocería de fibra de carbono que pesa solo 1.218 kg.",
                "logo": 'img/pagani.jpg'
            },
            {
                "title": "FERRARI LaFERRARI",
                "description": "Híbrido superdeportivo con tecnología de F1, equipado con un V12 de 6.3 litros y un motor eléctrico que combinados producen 963 CV, con aceleración de 0-100 km/h en menos de 3 segundos.",
                "logo": 'img/ferrari.jpg'
            },
            {
                "title": "ASTON MARTIN VALKYRIE",
                "description": "Desarrollado en colaboración con Red Bull Racing, cuenta con un V12 de 6.5 litros naturalmente aspirado que produce 1.160 CV y una aerodinámica extrema inspirada en la F1.",
                "logo": 'img/astonmartin.jpg'
            },
            {
                "title": "RIMAC NEVERA",
                "description": "Superdeportivo eléctrico croata con cuatro motores eléctricos que generan 1.914 CV, alcanza los 100 km/h en solo 1,85 segundos y tiene una velocidad máxima de 412 km/h.",
                "logo": 'img/rimac.jpg'
            },
            {
                "title": "KOENIGSEGG JESKO ABSOLUT",
                "description": "El Koenigsegg más rápido jamás creado, con un V8 biturbo de 5.0 litros que produce 1.600 CV con E85 y una velocidad teórica máxima de más de 500 km/h.",
                "logo": 'img/jesko.jpg'
            },
            {
                "title": "LAMBORGHINI SIÁN FKP 37",
                "description": "Primer superdeportivo híbrido de Lamborghini con un V12 de 6.5 litros y un supercapacitor en lugar de baterías, que genera 819 CV y acelera de 0-100 km/h en 2,8 segundos.",
                "logo": 'img/sian.jpg'
            },
            {
                "title": "McLAREN SPEEDTAIL",
                "description": "Híbrido de tres asientos con diseño inspirado en el F1, cuenta con 1.070 CV, aerodinámica activa, y una velocidad máxima de 403 km/h, siendo el McLaren más rápido de la historia.",
                "logo": 'img/speedtail.jpg'
            }
        ]

        context['additional_data'] = additional_data
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"