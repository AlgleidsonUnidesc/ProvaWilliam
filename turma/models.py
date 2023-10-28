from django.db import models

class turma(models.Model):
    codigoturma = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
