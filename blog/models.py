from django.db import models

class Blog(models.Model):
    
    titulo = models.CharField(max_length=136)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="photo_bike")
    url_strava = models.URLField()
    opinion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.titulo
    
