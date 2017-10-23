import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Municipality(models.Model):
    name = models.CharField(max_length=200)
    commune = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.name


class Ong(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    municipality = models.ForeignKey(Municipality,
                                     on_delete=models.SET_DEFAULT,
                                     default=''
                                     )

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.CharField(max_length=200, default='')
    birth = models.DateTimeField()
    description = models.CharField(max_length=500, default='')
    gender = models.CharField(max_length=10, default='hembra')
    ong = models.ForeignKey(Ong, on_delete=models.SET_DEFAULT, default='')

    PERRO = 'Perro'
    GATO = 'Gato'
    OTRO = 'Otro'
    ANIMALS_OPTIONS = (
        (PERRO,'Perro'),
        (GATO,'Gato'),
        (OTRO,'Otro')
    )

    animal_type = models.CharField(max_length=100,choices=ANIMALS_OPTIONS,default='PERRO')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    type = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    gender = models.CharField(max_length=10)
    hurt = models.BooleanField()
    comment = models.CharField(max_length=500)
    image = models.CharField(max_length=200)
    rescue = models.BooleanField()

    types_options = ('Abandono de Calle',
                     'Exposición a temperaturas extremas',
                     'Falta de Agua',
                     'Falta de Comida',
                     'Violencia',
                     'Venta ambulante')
    animals_options = ('Perro', 'Gato', 'Otro')
