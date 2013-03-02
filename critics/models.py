from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def get_from_email(self, email):
        return self.get(email=email, deleted=None)


class critic(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = 'email'

    nickname				=models.CharField(max_length=200)
    email                   =models.EmailField(max_length=200, unique=True)
    external_id = models.CharField(max_length=32, unique=True)
    nombre					=models.CharField(max_length=200)
    apellidos				=models.CharField(max_length=200)
    fecha_de_nacimiento		=models.DateTimeField()
    codigo_emblemas			=models.CommaSeparatedIntegerField(max_length=1000)
    manitos_arriba			=models.IntegerField()
    reviews					=models.IntegerField()
    imagen					=models.ImageField(upload_to = '/static/images/profile/')
    frase_favorita	        =models.CharField(max_length=100)
    cine_de_preferencia		=models.CharField(max_length=100)
    peliculas_preferidas	=models.CharField(max_length=200)

    objects = UserManager()

    REQUIRED_FIELDS = ['date_of_birth', 'height']

    @staticmethod
    def is_new_email(email):
        try:
            critic.objects.get_from_email(email.lower().strip())
            return False
        except critic.DoesNotExist:
            return True

    def save(self, *args, **kwargs):
        if not self.external_id:
            while 1:
                self.external_id = uuid.uuid4().hex
                try:
                    critic.objects.get(external_id=self.external_id)
                except self.DoesNotExist:
                    break
        super(critic, self).save(*args, **kwargs)




    def __unicode__(self):
        return self.email