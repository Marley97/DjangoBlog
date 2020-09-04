from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('profile/', views.profile, name="profil"),
    path('enregisterement/', views.register, name='register'),
    path('addSchool/', views.registerSchool, name='addSchool'),
    path('addClass/', views.registerClass, name="addClass"),
    path('listEtudiant/', views.ListStudent, name='listeE'),
    path('updateEt/<int:student_id>',views.modifier,name='update'),
    path('supprimerEt/<int:student_id>',views.delete,name='delete'),
    path('registerP/',views.registerProfile,name='registerPro'),
    path('connexion/',views.connexion,name='login'),
    path('deconnexion/',views.deconnexion,name='logout'),

]
