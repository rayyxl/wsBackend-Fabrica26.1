from django.urls import path
from .views import HomeView, PersonagemDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('/<str:name>/', PersonagemDetailView.as_view(), name='detalhes_personagem'),
]
