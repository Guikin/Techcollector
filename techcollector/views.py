from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tech,Providers,Perks
from django.views.generic import CreateView,DeleteView,UpdateView
from .forms import ProvidersForm


# Create your views here.
def home(request):
    techs = Tech.objects.all()
    return render(request,'home.html', {'techs':techs})

def techdetail(request,tech_id):
    tech = Tech.objects.get(id=tech_id)
    providers_form = ProvidersForm()

    perks_not_added = Perks.objects.exclude(id__in = tech.perk.all().values_list('id'))

    return render(request,'techdetail.html',{'tech':tech,'providers_form':providers_form, 'perks':perks_not_added})
    
def add_provider(request,tech_id):
    form = ProvidersForm(request.POST)
    if form.is_valid():
        new_provider = form.save(commit=False)
        new_provider.tech_id = tech_id 
        new_provider.save()
    return redirect('techdetail', tech_id=tech_id)                  

def delete_provider(request, tech_id, provider_id):
    provider = Providers.objects.get(id=provider_id)
    provider.delete()
    return redirect('techdetail',tech_id=tech_id)

def assoc_perk(request,tech_id,perk_id):
    Tech.objects.get(id=tech_id).perk.add(perk_id)
    return redirect('techdetail',tech_id=tech_id)


class TechCreate(CreateView):
       model = Tech
       fields = '__all__'


class TechUpdate(UpdateView):
    model= Tech
    fields = ['type','specs','price']       
       

class TechDelete(DeleteView):
    model= Tech
    success_url = '/'

class PerkCreate(CreateView):
    model = Perks
    fields = ['name','value']
    success_url = '/'    
