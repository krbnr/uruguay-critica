from critics.forms import RegistrationForm, LoginForm
from critics.models import critic
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def registrarcritico(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/perfil/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['nickname'],
                email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user.save()
            #critic = user.get_profile()
            #critic.nickname = form.cleaned_data['nickname']
            #critic.nombre = form.cleaned_data['nombre']
            #critic.apellidos = form.cleaned_data['apellidos']
            Critic = critic(user=user, nickname=form.cleaned_data['nickname'], nombre=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellidos'])
            Critic.save()
            """
            critic.cine_de_preferencia = form.cleaned_data['cine_de_preferencia']
            critic.peliculas_preferidas = form.cleaned_data['peliculas_preferidas']
            critic.fecha_de_nacimiento = form.cleaned_data['fecha_de_nacimiento']
            critic.Descripcion_personal = form.cleaned_data['Descripcion_personal']
            """
            #This is the correct way?
            auth_user = authenticate(username=form.cleaned_data['nickname'], password=form.cleaned_data['password'])
            login(request, auth_user)
            return HttpResponseRedirect('/perfil/')
        else:
            return render_to_response('registro.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('registro.html', context, context_instance=RequestContext(request))


def loginrequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/perfil/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            critic = authenticate(username=username, password=password)
            if critic is not None:
                login(request, critic)
                return HttpResponseRedirect('/perfil/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        #show login form
        form = LoginForm()
        context = {'form' : form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))

def logutrequest(request):
    logout(request)
    return HttpResponseRedirect('/')

def verperfil(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        pass
    else:
        #form = RegistrationForm()
        #TODO get user data
        usuario = request.user
        perfil = usuario.get_profile()
        #user_profile = usuario.get_profile()
        context = {'user': usuario, 'perfil': perfil}
        return render_to_response('perfil.html', context, context_instance=RequestContext(request))