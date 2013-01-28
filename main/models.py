from django.db import models

class pelicula(models.Model):
	titulo						=models.CharField(max_length=200)
	genero						=models.CharField(max_length=200)
	director					=models.CharField(max_length=200, null=True, blank=True)
	fecha_de_estreno			=models.DateTimeField(null=True, blank=True)
	reparto						=models.CharField(max_length=500, null=True, blank=True)
	pais						=models.CharField(max_length=100, null=True, blank=True)
	duracion					=models.CharField(max_length=100, null=True, blank=True)
	synopsis					=models.TextField(max_length=1000, null=True, blank=True)
	rating						=models.FloatField(null=True, blank=True)
	trailer						=models.CharField(max_length=1000, null=True, blank=True)
	
	def __unicode__(self):
		return self.titulo
