from django.urls import path
from . import views

urlpatterns = [
    path('submit_film/', views.submit_film),
    path('get_all_submitted_film/', views.get_all_submitted),
    path('get_all_selected/', views.get_all_selected),
    path('get_all_selected/', views.get_all_selected),
    path('film_detail/<str:slug>/', views.film_detail),
    path('add_to_selected/<str:slug>/update/', views.add_to_selected),
]