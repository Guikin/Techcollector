from django.contrib import admin
from .models import Tech,Providers,Perks

# Register your models here.
admin.site.register(Tech)
admin.site.register(Providers)
admin.site.register(Perks)