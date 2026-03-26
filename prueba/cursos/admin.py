from django.contrib import admin
from .models import Curso
from .models import Comentario

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    ordering = ('fecha_creacion') 

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','id')

admin.site.register(Comentario, AdministrarComentarios)