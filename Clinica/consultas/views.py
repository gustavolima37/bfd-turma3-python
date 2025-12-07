from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta
from .forms import ConsultaForm

from rest_framework import viewsets
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/lista.html', {'consultas': consultas})

def detalhe_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    return render(request, 'consultas/detalhe.html', {'consulta': consulta})

def nova_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'consultas/form.html', {'form': form})

