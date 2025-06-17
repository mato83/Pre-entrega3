from django.urls import path
from .views import cursos, profesores, estudiantes,inicio,  cursoFormulario2, profesorFormulario, busquedaCamada, buscar

urlpatterns = [
    # path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    # path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('', inicio, name='inicio'),
    path('cursos/', cursoFormulario2, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
  
    path('profesorFormulario', profesorFormulario, name="profesorFormulario"),






    # path('busquedaCamada', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar, name='buscar'),
]
