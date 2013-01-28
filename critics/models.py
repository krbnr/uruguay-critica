from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class critic(models.Model):
    user					=models.OneToOneField(User)
    nickname				=models.CharField(max_length=200)
    nombre					=models.CharField(max_length=200)
    apellidos				=models.CharField(max_length=200, null=True, blank=True)
    fecha_de_nacimiento		=models.DateTimeField(null=True, blank=True)
    codigo_emblemas			=models.CommaSeparatedIntegerField(max_length=1000, null=True, blank=True)
    manitos_arriba			=models.IntegerField(null=True, blank=True)
    reviews					=models.IntegerField(null=True, blank=True)
    imagen					=models.URLField(max_length=200, null=True, blank=True)
    Descripcion_personal	=models.CharField(max_length=100, null=True, blank=True)
    cine_de_preferencia		=models.CharField(max_length=100, null=True, blank=True)
    peliculas_preferidas	=models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nickname
"""
def create_user_profile(sender, instance, created, **kwargs):
    #Create the UserProfile when a new User is saved
    if created:
        profile = critic()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
"""