from django.db import models

class WebPage(models.Model):
    web_page    = models.CharField(max_length=30, unique=True)
    title       = models.CharField(max_length=100)
    description = models.TextField()
    is_menu_item = models.BooleanField(default=False)

    class meta:
        verbose_name        = "Bienvenida"
        verbose_name_plural = "Bienvenida"
    
    def __str__(self):
        return self.web_page
    
class Project(models.Model):
    title       = models.CharField(max_length=100)
    summary     = models.TextField(blank=True, null=True)
    description = models.TextField()
    technology  = models.CharField(max_length=20)
    image_path  = models.FileField(upload_to='', default='default/default.jpg', blank=True, null=True)
    start_date  = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    finish_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    class meta:
        verbose_name        = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-start_date"]
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    image_path  = models.FileField(upload_to='', default='default/icons.jpg', blank=True, null=True)
    order       = models.IntegerField(primary_key=False, blank=True, null=True)
    

    class meta:
        verbose_name        = "Skill"
        verbose_name_plural = "Skills"
        ordering = ["-order"]
    
    def __str__(self):
        return self.title