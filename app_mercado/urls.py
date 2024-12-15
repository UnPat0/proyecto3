from django.urls import path
from . import views

urlpatterns = [
    path('mi_vista/', views.mi_vista, name='mi_vista'),  # Aquí registramos la URL para tu vista
]