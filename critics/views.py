from critics.forms import RegistrationForm, LoginForm
from critics.models import critic
import re
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def createCritic(request):
    form = RegistrationForm
    if request.user.is_authenticated():
        return HttpResponseRedirect('/perfil/')
    if request.method == 'POST':
        form.append_dictionary(request.POST, ['email', 'password', 'password2'])

        #new django 1.5 user

        #email
        if not form.email or re.match('^\s*$', form.email):
            form.errors.email_required = True
        elif not re.match('^.{0,75}$', form.email):
            form.errors.email_max_lenght = True
        elif not critic.is_new_email(form.email):
            form.errors.email_exists = True
        else:
            critic.set_email(form.email)

        #password
        if not form.password or re.match('^\s*$', form.password):
            form.errors.password_required = True
        elif not re.match('^.{0,60}$', form.password):
            form.errors.password_max_lenght = True
        elif not re.match('^.{8,60}$', form.password):
            form.errors.password_min_lenght = True
        elif form.password != form.passwordagain:
            form.errors.password_no_match = True
        else:
            critic.set_password(form.password)

        #passwordagain
        if not form.password2 or re.match('^\s*$', form.password2):
            form.errors.password2_required = True

        #save
        if not len(form.errors) > 0:
            pass





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
            #TODO django confirmation mail
            auth_user = authenticate(username=form.cleaned_data['nickname'], password=form.cleaned_data['password'])
            login(request, auth_user)
            return HttpResponseRedirect('/perfil/')
        else:
            return render_to_response('registro.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form': form}
        #TODO add messages
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
        profile_form = RegistrationForm(request.POST, request.FILES, instance = request.user.get_profile())
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            usuario = request.user
            perfil = usuario.get_profile()
            form = RegistrationForm()
            context = {'user': usuario, 'perfil': perfil, 'form' : form}
            return render_to_response('perfil.html', context, context_instance=RequestContext(request))
    else:
        #TODO get user data and add it to the context
        usuario = request.user
        perfil = usuario.get_profile()
        form = RegistrationForm()
        context = {'user': usuario, 'perfil': perfil, 'form' : form}
        return render_to_response('perfil.html', context, context_instance=RequestContext(request))