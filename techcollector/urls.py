from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('tech/<int:tech_id>',views.techdetail, name='techdetail'),
    path('tech/create',views.TechCreate.as_view(),name='tech_create'),
    path('tech/perk/create',views.PerkCreate.as_view(),name='perk_create'),
    path('tech/<int:pk>/update',views.TechUpdate.as_view(),name='tech_update'),
    path('tech/<int:pk>/delete',views.TechDelete.as_view(),name='tech_delete'),
   
    path('tech/<int:tech_id>/add_provider',views.add_provider, 
    name='add_provider'),
    path('tech/<int:tech_id>/provider/<int:provider_id>,',views.delete_provider,name="delete_provider"),
    path('tech/<int:tech_id>/assoc_perk/<int:perk_id>',views.assoc_perk,name='assoc_perk')
]
