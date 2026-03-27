from django.db import models


class Modalidad(models.TextChoices):
    EN_LINEA = 'EN_LINEA', 'En línea'
    PRESENCIAL = 'PRESENCIAL', 'Presencial'


class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del curso")
    descripcion = models.TextField(verbose_name="Descripción del curso")
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True, verbose_name="Imagen del curso")
    duracion_horas = models.PositiveIntegerField(verbose_name="Duración (horas)")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    modalidad = models.CharField(max_length=12, choices=Modalidad.choices, verbose_name="Modalidad")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")




    def __str__(self):
        return self.nombre