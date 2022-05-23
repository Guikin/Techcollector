from django.forms import ModelForm
from .models import Providers

class  ProvidersForm(ModelForm):
    class Meta:
        model = Providers
        fields =['name','price','stock']
