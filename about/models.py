from django.db import models

class About(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:        
        ordering = ['-created']

    def __str__(self):
        return self.titulo
    