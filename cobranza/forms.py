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
        self.helper.add_input(Submit('submit', 'Agregar usuario'))


class ModificarRuta(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar usuario'))

class CrearVisita(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar usuario'))


class ModificarVisita(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar usuario'))
