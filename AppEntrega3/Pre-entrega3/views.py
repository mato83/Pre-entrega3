from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso
from .forms import CursoFormulario, ProfesorFormulario, EstudiantesFormulario

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiante_detail.html', {'estudiante': estudiante})


def inicio(request):
    return render(request, "AppEntrega3/index.html")

def cursos(request):
    return render(request, "AppEntrega3/cursos.html")

def profesores(request):
    return render(request, "AppEntrega3/profesores.html")

def estudiantes(request):
    return render(request, "AppEntrega3/estudiantes.html")



def cursoFormulario(request):
    
       if request.method == 'POST':
            curso =  Curso(nombre=request.POST['nombre'],camada=(request.POST['camada']))
            curso.save()
            return render(request, "AppEntrega3/index.html")
            return render(request, "AppEntrega3/formulario/cursoFormulario.html")

















def cursoFormulario2(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/index.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/formulario/cursoFormulario2.html", {"miFormulario": miFormulario})






def profesorFormulario(request):

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)  # aquí llega toda la información del html
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()
            return render(request, "AppCoder/index.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el html

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})






































def busquedaCamada(request):
    return render(request, "AppCoder/formulario/busquedaCamada.html")


def buscar(request):
    if request.GET["camada"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
        camada = request.GET['camada']
        # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
        # sin importar si las letras están en mayúsculas o minúsculas
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/formulario/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:
        respuesta = "No enviaste datos"

        # No olvidar from django.http import HttpResponse
        return HttpResponse(respuesta)
