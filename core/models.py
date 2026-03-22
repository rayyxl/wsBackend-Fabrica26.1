from django.db import models

class Opinion(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    opiniao = models.CharField(max_length=60)

    def __str__(self):
        return self.nome
    