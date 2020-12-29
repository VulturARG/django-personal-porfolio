from django.db import models

class Welcome(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()

    class meta:
        verbose_name        = "Bienvenida"
        verbose_name_plural = "Bienvenida"
    
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    technology  = models.CharField(max_length=20)
    image_path  = models.FileField(upload_to='photo', default='default/default.jpg', max_length=100, blank=True, null=True)
    start_date  = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    finish_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    class meta:
        verbose_name        = "Proyecto"
        verbose_name_plural = "Proyectos"
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    image_path  = models.FileField(upload_to='icons', default='default/icons.jpg', max_length=100, blank=True, null=True)

    class meta:
        verbose_name        = "Skill"
        verbose_name_plural = "Skills"
    
    def __str__(self):
        return self.title