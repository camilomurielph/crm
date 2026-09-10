from django import forms
from .models import Cliente, Proyecto, Tarea, Enlace


class OptionalFieldsMixin:
    """Fuerza todos los campos a no ser obligatorios."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class ClienteForm(OptionalFieldsMixin, forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fecha_primer_contacto': forms.DateInput(attrs={'type': 'date'}),
            'fecha_firma_contrato': forms.DateInput(attrs={'type': 'date'}),
        }


class ProyectoForm(OptionalFieldsMixin, forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        exclude = ['cliente']


class TareaForm(OptionalFieldsMixin, forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria']


class EnlaceForm(OptionalFieldsMixin, forms.ModelForm):
    class Meta:
        model = Enlace
        fields = ['nombre', 'url']
