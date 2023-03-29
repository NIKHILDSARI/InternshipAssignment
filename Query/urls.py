from django.urls import path
from . import views

urlpatterns = [
    path('bancklist/', views.Banklist),
    path('branchdetails/', views.Branchdetails),
    path('spicific_branchdetails/', views.spicific_Branchdetails),
]
