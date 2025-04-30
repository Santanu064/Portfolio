from django.shortcuts import render
from .models import Skills,Project
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    f_skill = Skills.objects.all()[:7]
    s_skill = Skills.objects.all()[7:]
    project = Project.objects.all()
    return render(request, 'home.html',{'skills':f_skill,'skills2':s_skill , 'pro':project}) 