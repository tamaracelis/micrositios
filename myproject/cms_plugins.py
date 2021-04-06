from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from .models import *

#Tamara Celis

#class GaleriaPlugin: usada para crear introdución de una galeria
@plugin_pool.register_plugin
class GaleriaPlugin (CMSPluginBase):
    model = Gallery
    render_template = "photos.html"
    cache = False

#class redes sociales: usada para crear botones que se enlazan con sus redes sociales respectivas
@plugin_pool.register_plugin
class InstagramPlugin (CMSPluginBase):
    model = InstagramBottons
    render_template = "Instagram.html"
    cache = False

@plugin_pool.register_plugin
class FacebookPlugin (CMSPluginBase):
    model = FacebookBottons
    render_template = "Facebook.html"
    cache = False

@plugin_pool.register_plugin
class TwitterPlugin (CMSPluginBase):
    model = TwitterBottons
    render_template = "Twitter.html"
    cache = False

@plugin_pool.register_plugin
class LinkedinPlugin (CMSPluginBase):
    model = LinkedinBottons
    render_template = "Linkedin.html"
    cache = False

#class TextoPlugin: encargada de crear textos
@plugin_pool.register_plugin
class TextoPlugin(CMSPluginBase):
    model = Texto
    render_template = "News.html"
    cache = False

#Pablo Gutiérrez

#class players: usada para crear el elemento
@plugin_pool.register_plugin
class players(CMSPluginBase):
    model = Players
    render_template = "players_plugin.html"
    cache = False


#Class prizes: utilizado para mostrar los premios del equipo
@plugin_pool.register_plugin
class prizes(CMSPluginBase):
    model = Prizes
    render_template = "prizes_plugin.html"
    cache = False