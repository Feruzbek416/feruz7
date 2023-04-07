from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from dars.models import News1,Python,FTF,Yangi

# Create your views here.

class Kurs1Page(ListView):
    template_name='kurs1.html'
    model = News1
class Kurs2Page(TemplateView):
    template_name='kurs2.html'
class Kurs3Page(TemplateView):
    template_name='kurs3.html'
class Kurs4Page(TemplateView):
    template_name='kurs4.html'
class RegistPage(ListView):
    template_name='registr.html'
    model=Python
class KompPage(ListView):
    template_name='komp.html'
    model=Python   
class ftfPage(ListView):
    template_name='ftf.html'
    model=FTF
    
    
def New(request):   
    context = Yangi.objects.all()
    return render(request,'news.html',{"context":context})

