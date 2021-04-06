from cms.models.pluginmodel import CMSPlugin
from tinymce.models import HTMLField
from django.db import models

#Tamara Celis

# Modelo de galeria
# Esto incluye un nombre del album (Nombre) y su descripcion
class Gallery(CMSPlugin):
    Nombre = models.CharField(max_length=50, default='Nombre del album')
    Descripcion = models.TextField(default="descripción")

# Modelo de botones de rrss
# Cada uno se le debe ingresar el link
class InstagramBottons(CMSPlugin):
    Instagram = models.CharField(max_length=1000, default="#")

class FacebookBottons(CMSPlugin):
    Facebook = models.CharField(max_length=1000, default="#")

class TwitterBottons(CMSPlugin):
    Twitter = models.CharField(max_length=1000, default="#")

class LinkedinBottons(CMSPlugin):
    Linkedin = models.CharField(max_length=1000, default="#")


#Modelo de texto para una publicacion
# Incluye un titulo y un cuerpo
class Texto (CMSPlugin):
    Title = models.CharField(max_length=50, default="Título")
    Body = HTMLField()

#Pablo Gutierrez

#Modelo del jugador del equipo
#Este incluye 3 parametros que el usuario agrega, el nombre del jugador, posición o caracteristica y
#Finalmente agrega una imagen del jugador.
class Players(CMSPlugin):
    player_name = models.CharField(max_length=50, default='Nombre del Jugador')
    player_position = models.CharField(max_length=50, default='Posicion de juego')
    player_image = models.ImageField(verbose_name="Imagen del jugador")


#Modelo de prizes, escribiendo el numero de copas (en int) y la descripcion del premio la agrega a
#los logros realizados por el equipo.
class Prizes(CMSPlugin):
    numero = models.IntegerField(default='Número de copas')
    descripcion = models.CharField(max_length=1000, default='Descripción del premio')