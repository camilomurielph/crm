from django import forms
from .models import Cliente, Proyecto, Tarea, Enlace

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fecha_primer_contacto': forms.DateInput(attrs={'type': 'date'}),
            'fecha_firma_contrato': forms.DateInput(attrs={'type': 'date'}),
        }

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        exclude = ['cliente']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria']

class EnlaceForm(forms.ModelForm):
    class Meta:
        model = Enlace
        fields = ['nombre', 'url']
