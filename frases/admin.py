from django.contrib import admin

from .models import Categoria, Fraseologia

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Fraseologia)
class FraseologiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_criacao', 'data_atualizacao')
    list_filter = ('categoria', 'data_criacao')
    search_fields = ('titulo', 'conteudo_template')
    date_hierarchy = 'data_criacao'
    ordering = ('titulo',)
