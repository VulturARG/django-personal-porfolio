from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.project_index, name="project_index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("skill/", views.skill_index , name="skill_index"),
    path("generic/<int:pk>/", views.generic_page , name="generic_page"),
]