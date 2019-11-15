from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CrearUsuario(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar usuario'))


class ModificarUsuario(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('rut_usuario', 'password', 'nombres', 'apellidos' , 'direccion' , 'telefono_movil', 'telefono_residencial', 'correo', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar usuario'))


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)