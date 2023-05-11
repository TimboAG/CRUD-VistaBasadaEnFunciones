from django.db import models

# Create your models here.
class Autor(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=200, blank= False, null=False)
    apellido= models.CharField(max_length=200, blank=False, null=False)
    nacionalidad= models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
    
    def __str__(self) :
        return self.nombre +  " " + self.apellido
    
    
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 255, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank = False, null = False)
    #Uno a uno (un autor un libros)
    # autor = models.OneToOneField(Autor, on_delete=models.CASCADE)
    
    #Uno a muchos (un autor muchos libros)
    # autor = models.ForeingKey(Autor, on_delete=models.CASCADE)
    
    #Mucho a muchos (Un libro puede pertencer a varios autores, y varios autores pueden tener varios libros)
    autor = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo 