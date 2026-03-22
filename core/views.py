from django.shortcuts import render, redirect
from django.views import View
from urllib3 import request
from .services.api import listar_personagens, buscar_personagem_por_nome
from .models import Opinion
from .forms import OpinionForm
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        personagens = listar_personagens()
        return render(request, 'core/home.html', {'personagens': personagens})
        

class PersonagemDetailView(View):
    def get(self, request, name):
        personagem = buscar_personagem_por_nome(name)
        return render(request, 'core/personagem_detail.html', {'personagem': personagem})
        

class OpinionCreateView(View):
    def get(self, request):
        form = OpinionForm()
        return render(request, 'core/opinion_edit.html', {'form': form, 'opinions': Opinion.objects.all()})
    
    def post(self, request):
        form = OpinionForm(request.POST)
        opinioes = Opinion.objects.all()
        if form.is_valid():
            form.save()
            return render(request, 'core/list_opinions.html', {'form': OpinionForm(), 'opinions': opinioes})
        
        else:
            messages.error(request, "Por favor, corrija os erros no formulário.")
    # Mude de 'list_opinions.html' para 'opinion_edit.html'
            return render(request, 'core/opinion_edit.html', {
                'form': form, 
                'opinions': Opinion.objects.all()
            })
    
        
class OpinionEditView(View):
    def get(self, request, nome):
        opinioes = Opinion.objects.all()
        personagem = Opinion.objects.filter(nome=nome).first()
        form = OpinionForm(instance=personagem)
        return render(request, 'core/opinion_edit.html', {'form': form, 
                                                          'personagem': personagem, 
                                                          'opinions': opinioes})
        
    def post(self, request, nome):
        form = OpinionForm(request.POST, instance=Opinion.objects.filter(nome=nome).first())
        if form.is_valid():
            form.save()
            return redirect('list_opinions')
        else:

            return render(request, 'core/opinion_edit.html', {
                'form': form, 
                'personagem': buscar_personagem_por_nome(nome),
                'opinions': Opinion.objects.all()
            })    
    
class OpinionDeleteView(View):
    def get(self, request, nome):
        opinion = Opinion.objects.filter(nome=nome).first()
        if opinion:
            opinion.delete()
            messages.success(request, f'Opinião sobre {nome} deletada com sucesso!')
        return render(request, 'core/list_opinions.html', {
            'form': OpinionForm(), 
            'personagem': buscar_personagem_por_nome(nome), 
            'opinions': Opinion.objects.all()})
    
class OpinionManageView(View):
    def get(self, request):
        opinioes = Opinion.objects.all()
        return render(request, 'core/list_opinions.html', {'opinions': opinioes})
