from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['nome', 'opiniao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 130, 'required': True}),
            'opiniao': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 30, 'required': True}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome').strip()

        if Opinion.objects.filter(nome__iexact=nome).exists():
            raise forms.ValidationError("Já existe uma opinião para este personagem.")
        
        else: 
            return nome.title()