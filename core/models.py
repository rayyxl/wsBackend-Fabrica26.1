from django.db import models

class Opinion(models.Model):
    nome = models.CharField(max_length=130, unique=True)
    opiniao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome