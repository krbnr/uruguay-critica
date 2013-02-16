from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from critics.models import critic


class RegistrationForm(ModelForm):
    nickname			    =forms.CharField(label=(u'Nombre de Usuario(Nickname) '))
    nombre					=forms.CharField(label=(u'Nombre '))
    apellidos				=forms.CharField(label=(u'Apellidos '))
    email					=forms.EmailField(label=(u'E-mail '))
    password				=forms.CharField(label=(u'Password '), widget=forms.PasswordInput(render_value=False), initial=None)
    password2				=forms.CharField(label=(u'Confirmar Password: '), widget=forms.PasswordInput(render_value=False), initial=None)
    cine_de_preferencia		=forms.CharField(label=(u'Cine preferido (ej: Movie Center Portones) '), required=False)
    peliculas_preferidas	=forms.CharField(label=(u'Peliculas favoritas(separadas por coma) '), required=False)
    #to attach a label to a form field, this is the best practice?

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        #Warning here the order of fields also hide the ones that not are on the list
        self.fields.keyOrder = [
        'nickname',
        'nombre',
        'apellidos',
        'email',
        'password',
        'password2',
        'peliculas_preferidas',
        ]

    class Meta:
        model = critic
        exclude = ('user', 'manitos_arriba', 'reviews', 'codigo_emblemas',
                   'imagen', 'cine_de_preferencia','peliculas_preferidas',
                   'Descripcion_personal', 'fecha_de_nacimiento',)


    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        try:
            User.objects.get(username=nickname)
        except User.DoesNotExist:
            return nickname
        raise forms.ValidationError("Ese nickname ya existe, elige otro.")


    def cleaned_password(self):
        password = self.cleaned_data['password']
        print password
        password2 = self.cleaned_data['password2']
        print password2
        if password != password2:
            raise forms.ValidationError('Los passwords no coinciden')
        return password

class LoginForm(forms.Form):
    username = forms.CharField(label= u'Nombre de Usuario')
    password = forms.CharField(label= u'Password', widget = forms.PasswordInput(render_value=False))
