from django.shortcuts import render
from django.http import HttpResponse
from .models import Tech


# Create your views here.
def home(request):
    techs = Tech.objects.all()
    return render(request,'home.html', {'techs':techs})

def techdetail(request,tech_id):
    tech = Tech.objects.get(id=tech_id)
    return render(request,'techdetail.html',{'tech':tech})