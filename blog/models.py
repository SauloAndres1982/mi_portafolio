from django.db import models
from django.utils import timezone



class Opinion(models.Model):
    opinion_text = models.TextField()
    created = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.opinion_text

class Blog(models.Model):
    
    titulo = models.CharField(max_length=136)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="photo_bike")
    url_strava = models.URLField()
    opiniones = models.ManyToManyField(Opinion, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.titulo
    
