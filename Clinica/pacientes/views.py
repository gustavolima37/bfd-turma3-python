from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer  # corrigido


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer  # corrigido
