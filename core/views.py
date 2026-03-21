from django.shortcuts import render
from django.views import View
from .services.api import listar_personagens, buscar_personagem_por_nome
class HomeView(View):
    def get(self, request):
        if request.method == 'GET':
            personagens = listar_personagens()
            return render(request, 'core/home.html', {'personagens': personagens})
        

class PersonagemDetailView(View):
    def get(self, request, name):
        if request.method == 'GET':
            personagem = buscar_personagem_por_nome(name)
            return render(request, 'core/personagem_detail.html', {'personagem': personagem})
        