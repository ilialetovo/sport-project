from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/football/', views.football, name='football'),
    path('country/volleyball/', views.volleyball, name='volleyball'),
    path('country/basketball/', views.basketball, name='basketball'),
    path('country/ski/', views.ski, name='ski'),
    path('country/swimming/', views.swimming, name='swimming')
]
