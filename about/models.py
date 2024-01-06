from django.db import models

class About(models.Model):
    titulo = models.CharField(max_length=100)
    degree_title = models.CharField(max_length=300, verbose_name="Título obtenido")
    photo_perfil = models.ImageField(upload_to="poto_perfil", verbose_name="Foto de perfil", blank=True, null=True)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:        
        verbose_name = "formación"
        verbose_name_plural = "formaciones"
        ordering = ['-created']

    def __str__(self):
        return self.titulo
    

class Skills(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    imagen = models.ImageField(upload_to="skills", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:        
        verbose_name = "conocimiento"
        verbose_name_plural = "conocimientos"
        ordering = ['created']
    def __str__(self):
        return self.titulo