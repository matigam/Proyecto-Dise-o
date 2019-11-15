from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class CrearRuta(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar ruta'))


class ModificarRuta(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar ruta'))

class CrearVisita(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar Visita'))


class ModificarVisita(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar Visita'))

class CrearPropietario(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar Propietario'))


class ModificarPropietario(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar Propietario'))
