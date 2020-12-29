from django.contrib import admin
from .models import Project, Welcome, Skill


admin.site.register(Welcome)
admin.site.register(Skill)

class ProjectsAdmin(admin.ModelAdmin):
    fields = ['title','description','technology','start_date','finish_date','image_path']
    list_display = ['title','description','technology','start_date','finish_date','image_path']
    ordering = ['-start_date']

admin.site.register(Project,ProjectsAdmin)
