from rest_framework import viewsets
from .models import Medico
from .serializers import MedicoSerializer  # corrigido



class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer  # corrigido