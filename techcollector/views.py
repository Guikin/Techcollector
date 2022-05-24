from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tech,Providers,Perks
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,DetailView
from .forms import ProvidersForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def home(request):
    techs = Tech.objects.all()
    return render(request,'home.html', {'techs':techs})

@login_required 
def techdetail(request,tech_id):
    tech = Tech.objects.get(id=tech_id)
    providers_form = ProvidersForm()

    perks_not_added = Perks.objects.exclude(id__in = tech.perk.all().values_list('id'))

    return render(request,'techdetail.html',{'tech':tech,'providers_form':providers_form, 'perks':perks_not_added})

@login_required    
def add_provider(request,tech_id):
    form = ProvidersForm(request.POST)
    if form.is_valid():
        new_provider = form.save(commit=False)
        new_provider.tech_id = tech_id 
        new_provider.save()
    return redirect('techdetail', tech_id=tech_id)                  

@login_required  
def delete_provider(request, tech_id, provider_id):
    provider = Providers.objects.get(id=provider_id)
    provider.delete()
    return redirect('techdetail',tech_id=tech_id)

@login_required  
def assoc_perk(request,tech_id,perk_id):
    Tech.objects.get(id=tech_id).perk.add(perk_id)
    return redirect('techdetail',tech_id=tech_id)


def signup(request):
    error_message= ''
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - Try again'
    form=UserCreationForm()
    context = {'form':form, 'error_message':error_message}
    return render(request,'registration/signup.html',context)                


class TechCreate(LoginRequiredMixin,CreateView):
       model = Tech
       fields = ['name','type','specs','price']
       def form_valid(self,form):
           form.instance.user = self.request.user
           return super().form_valid(form)


class TechUpdate(LoginRequiredMixin,UpdateView):
    model= Tech
    fields = ['type','specs','price']       
       

class TechDelete(LoginRequiredMixin,DeleteView):
    model= Tech
    success_url = '/'

class PerkCreate(LoginRequiredMixin,CreateView):
    model = Perks
    fields = ['name','value']
    success_url = '/'    
