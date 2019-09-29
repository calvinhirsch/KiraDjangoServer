from django.urls import path
from . import views

urlpatterns = [
    path('folders/', views.folders, name='folders'),
    path('addFolder/', views.addFolder, name='addFolder'),
    path('deleteFolder/', views.deleteFolder, name='deleteFolder'),
    path('photosFromFolder/', views.photosFromFolder, name='photosFromFolder'),
    path('analyzePhoto/', views.analyzePhoto, name='analyzePhoto'),
    path('submitPhoto/', views.submitPhoto, name='submitPhoto'),
    path('deletePhoto/', views.deletePhoto, name='deletePhoto'),
    path('getTrials/', views.getTrials, name='getTrials'),
    path('', views.index, name='index'),
]