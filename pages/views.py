from django.shortcuts import render
from django.http import HttpResponse

from managers.models import Manager

def index(request):
    
    return render(request,'pages/index.html')


def about(request):
    #get all managers
    managers = Manager.objects.order_by('-hire_date')
    context = {
        'managers':managers,
    }
    return render(request,'pages/about.html', context)
