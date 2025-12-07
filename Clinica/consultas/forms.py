from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["paciente", "medico", "data", "descricao", "status"]
        widgets = {
            "data": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }