from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Paciente, Practica, Medico
from AppCoder.forms import  PracticaFormulario, PacienteFormulario, MedicoFormulario



# Create your views here.


def inicio(request):

      return render(request, "AppCoder/inicio.html")


def pacientes(request):

      if request.method == 'POST':

            miFormulario = PacienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  paciente = Paciente (nombre=informacion['nombre'], Apellido=informacion['Apellido'], documento_pac=informacion['documento_pac']) 

                  paciente.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PacienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/pacientes.html", {"miFormulario":miFormulario})




def buscar(request):
      if(len(request.GET["documento_pac"]))==8:
            documento_pac = request.GET['documento_pac'] 
            paciente = Paciente.objects.filter(documento_pac__icontains=documento_pac)
            return render(request, "AppCoder/inicio.html", {"pacientes":paciente, "documento_pac":documento_pac})
      else: 
            respuesta = "Ingrese un documento valido"
            return render(request, "AppCoder/inicio.html", {"error":respuesta})
      #No olvidar from django.http import HttpResponse

def practicas(request):


      if request.method == 'POST':

            miFormulario = PracticaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  practica = Practica (documento_pac=informacion['documento_pac'], fecha_practica=informacion['fecha_practica']) 

                  practica.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PracticaFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/practicas.html", {"miFormulario":miFormulario})

def medicos(request):

      if request.method == 'POST':

            miFormulario = MedicoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  medico = Medico (nombre=informacion['nombre'], Apellido=informacion['Apellido'], Profesion=informacion['Profesion']) 

                  medico.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= MedicoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/medicos.html", {"miFormulario":miFormulario})