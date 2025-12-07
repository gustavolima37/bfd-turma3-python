from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico

# Create your models here.

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="consultas")
    data = models.DateTimeField()
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("angendada", 'Agendada'),
            ("realizada", "Realizada"),
            ("cancelada", "Cancelada")
        ],
        default="agendada"
    )
    
    def __str__(self):
        return f"{self.paciente} - {self.medico} ({self.data:%d/%m/%Y %H:%M})"