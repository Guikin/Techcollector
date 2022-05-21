from django.shortcuts import render
from django.http import HttpResponse
from .models import Tech
from django.views.generic import CreateView,DeleteView,UpdateView


# Create your views here.
def home(request):
    techs = Tech.objects.all()
    return render(request,'home.html', {'techs':techs})

def techdetail(request,tech_id):
    tech = Tech.objects.get(id=tech_id)
    return render(request,'techdetail.html',{'tech':tech})

class TechCreate(CreateView):
       model = Tech
       fields = '__all__'


class TechUpdate(UpdateView):
    model= Tech
    fields = ['type','specs','price']       
       

class TechDelete(DeleteView):
    model= Tech
    success_url ='/'
