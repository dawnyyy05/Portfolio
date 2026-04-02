

from django.shortcuts import render
from .models import Info, Education, Project, Skill, Contact

def index(request):
    return render(request, 'index.html', {
        'info': Info.objects.first(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'education': Education.objects.all(),
        'contact': Contact.objects.first(),
    })
