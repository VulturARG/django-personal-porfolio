from django.shortcuts import render
from .models import Project, Welcome, Skill


def index(request):
    index = Welcome.objects.first()
    context = {
        'welcome': index
    }
    return render(request, 'projects/index.html', context)

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)

def skill_index(request):
    skill = Skill.objects.all()
    context = {
        'projects': skill
    }
    return render(request, 'projects/skill_index.html', context)