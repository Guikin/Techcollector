from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('tech/<int:tech_id>',views.techdetail, name='techdetail'),
    path('tech/create',views.TechCreate.as_view(),name='tech_create'),
    path('tech/<int:pk>/update',views.TechUpdate.as_view(),name='tech_update'),
    path('tech/<int:pk>/delete',views.TechDelete.as_view(),name='tech_delete'),
   
]
