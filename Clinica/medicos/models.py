from django.db import models

# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"