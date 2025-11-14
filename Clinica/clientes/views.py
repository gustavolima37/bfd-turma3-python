from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer  # corrigido
from django.http import HttpResponse


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer  # corrigido

def home(request):
    return HttpResponse("Bem-vindo à API da Clínica!")