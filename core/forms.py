from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['nome', 'opiniao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'field-form', 'maxlength': 30, 'required': True}),
            'opiniao': forms.TextInput(attrs={'class': 'field-form', 'maxlength': 60, 'required': True}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome').strip()

        queryset = Opinion.objects.filter(nome__iexact=nome)

        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise forms.ValidationError("Este nome já existe!")
        
        else: 
            return nome.title()
        

