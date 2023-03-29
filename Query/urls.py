from django.urls import path
from . import views

urlpatterns = [
    path('banklist/', views.Banklist),
    path('branchdetails/', views.Branchdetails),
    path('specific_branchdetails/', views.specific_Branchdetails),
]
