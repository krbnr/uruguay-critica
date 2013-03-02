from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from critics.models import critic


class RegistrationForm(ModelForm):
    nickname			    =forms.CharField(label=(u'Nombre de Usuario(Nickname) '))
    email					=forms.EmailField(label=(u'E-mail '))
    password				=forms.CharField(label=(u'Password '), widget=forms.PasswordInput(render_value=False), initial=None)
    password2				=forms.CharField(label=(u'Confirmar Password: '), widget=forms.PasswordInput(render_value=False), initial=None)


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        #T order of fields also hide the ones that not are on the list
        self.fields.keyOrder = [
        'nickname',
        'email',
        'password',
        'password2',
        ]

    class Meta:
        model = critic
        #if the order of fields is set, it's not necessary to exclude them
        """
        exclude = ('user', 'manitos_arriba', 'reviews', 'codigo_emblemas',
                   'imagen', 'cine_de_preferencia','peliculas_preferidas',
                   'Descripcion_personal', 'fecha_de_nacimiento',)
        """


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

class ProfileForm(ModelForm):
    nickname			    =forms.CharField(label=(u'Nombre de Usuario(Nickname) '))
    nombre					=forms.CharField(label=(u'Nombre '))
    apellidos				=forms.CharField(label=(u'Apellidos '))
    email					=forms.EmailField(label=(u'E-mail '))
    password				=forms.CharField(label=(u'Password '), widget=forms.PasswordInput(render_value=False), initial=None)
    password2				=forms.CharField(label=(u'Confirmar Password: '), widget=forms.PasswordInput(render_value=False), initial=None)
    cine_de_preferencia		=forms.CharField(label=(u'Cine preferido (ej: Movie Center Portones) '), required=False)
    imagen					=forms.ImageField(label=(u'Imagen: '), required=False)
    peliculas_preferidas	=forms.CharField(label=(u'Peliculas favoritas(separadas por coma) '), required=False)


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'nickname',
            'nombre',
            'apellidos',
            'email',
            'password',
            'peliculas_preferidas'
            'cine_de_preferencia',
            'peliculas_preferidas',
            'Descripcion_personal',
            'fecha_de_nacimiento'
            'manitos_arriba', 'reviews', 'codigo_emblemas',
            'imagen'
        ]

    class Meta:
        model = critic

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        try:
            user = User.objects.get(username=nickname)
            if user.nickname() == nickname:
                return nickname
        except User.DoesNotExist:
            return nickname
        raise forms.ValidationError("Ese nickname ya existe, elige otro.")

class LoginForm(forms.Form):
    username = forms.CharField(label= u'Nombre de Usuario')
    password = forms.CharField(label= u'Password', widget = forms.PasswordInput(render_value=False))

