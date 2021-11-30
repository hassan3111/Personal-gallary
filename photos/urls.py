from django.urls import path

# from photos.views import gallary
from . import views

urlpatterns =[ 
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('search/', views.search_results, name='search'),
    


]