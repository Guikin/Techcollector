from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('tech/<int:tech_id>',views.techdetail, name='tech')
]