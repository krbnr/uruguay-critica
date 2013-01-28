# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'pelicula'
        db.create_table('main_pelicula', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('fecha_de_estreno', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('reparto', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('duracion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('synopsis', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('trailer', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['pelicula'])


    def backwards(self, orm):
        # Deleting model 'pelicula'
        db.delete_table('main_pelicula')


    models = {
        'main.pelicula': {
            'Meta': {'object_name': 'pelicula'},
            'director': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha_de_estreno': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reparto': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trailer': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']