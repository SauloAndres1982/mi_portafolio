from django.db import models

class Project(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    imagen = models.ImageField(max_length=2400) 
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.titulo