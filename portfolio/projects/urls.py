from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.project_index, name="project_index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("skill/", views.skill_index , name="skill_index"),
    path("generic/<int:pk>/", views.generic_page , name="generic_page"),
    path("populate_tables/", views.populate_tables , name="populate_tables"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)