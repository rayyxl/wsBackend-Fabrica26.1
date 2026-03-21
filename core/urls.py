from django.urls import path
from .views import HomeView, OpinionCreateView, PersonagemDetailView, OpinionEditView, OpinionDeleteView, OpinionManageView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('/<str:name>/', PersonagemDetailView.as_view(), name='detail_personagem'),
    path('create/', OpinionCreateView.as_view(), name='create_opinion'),
    path('<str:nome>/edit/', OpinionEditView.as_view(), name='edit_opinion'),
    path('<str:nome>/delete/', OpinionDeleteView.as_view(), name='delete_opinion'),
    path('opinions/', OpinionManageView.as_view(), name='list_opinions'),
]
