from django.urls import path
from . import views



app_name = 'members'

urlpatterns = [
    path('', views.index, name='index'),
    path('people/', views.people, name='people'),
]
