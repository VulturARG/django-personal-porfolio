from django.shortcuts import render
from .models import Project, WebPage, Skill, Icon


def index(request):
    index = WebPage.objects.get(web_page = 'index')
    menu_items = WebPage.objects.all().filter(is_menu_item = True)
    context = {
        'welcome': index,
        'menu_items':menu_items,
    }
    return render(request, 'projects/index.html', context)

def project_index(request):
    projects = Project.objects.all()
    menu_items = WebPage.objects.all().filter(is_menu_item = True)
    context = {
        'projects': projects,
        'menu_items':menu_items,
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    menu_items = WebPage.objects.all().filter(is_menu_item = True)
    context = {
        'project': project,
        'menu_items':menu_items,
    }
    return render(request, 'projects/project_detail.html', context)

def skill_index(request):
    skill_titles = WebPage.objects.get(web_page = 'skills')
    skills = Skill.objects.all()
    menu_items = WebPage.objects.all().filter(is_menu_item = True)
    context = {
        'skills': skills,
        'skill_titles':skill_titles,
        'menu_items':menu_items,
    }
    return render(request, 'projects/skill_index.html', context)

def generic_page(request, pk):
    generic_page = WebPage.objects.get(pk=pk)
    menu_items = WebPage.objects.all().filter(is_menu_item = True)
    context = {
        'generic_page': generic_page,
        'menu_items':menu_items,
    }
    return render(request, 'projects/generic_page.html', context)

def populate_tables(request):
    icon = {
        'docker':'fa-docker',
        'linkedin':'fa-linkedin',
        'python':'fa-python',
        'html5':'fa-html5',
        'css3':'fa-css3',
        'bootstrap':'fa-bootstrap',
        'mysql':'fa-database',
        'js':'fa-js-square',
        'ajax':'fa-code',
        'jquery':'fa-code',
        'php':'fa-php',
        'cakePHP':'fa-code',
        'C':'fa-code',
        'SQF':'fa-code',
    }
    try:
        for clave in icon:
            record = Icon(aplication=clave,icon_name=icon[clave])
            record.save()
        success = True
    except:
        success = False
    
    menu_items = WebPage.objects.all().filter(is_menu_item = True)
    context = {
        'success': success,
        'menu_items':menu_items,
    }
    return render(request, 'projects/populate_tables.html', context)
