from django.urls import include, re_path,path

from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('searchbar/',views.searchbar,name='searchbar')
]