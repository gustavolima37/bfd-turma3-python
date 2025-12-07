from django.shortcuts import render

def home(request):
    contexto = {"titulo": "Clínica Saúde+"}
    return render(request, "clinica/home.html", contexto)