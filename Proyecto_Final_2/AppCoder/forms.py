from django import forms


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class PacienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)  
    documento_pac = forms.IntegerField()

class MedicoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)  
    Profesion = forms.CharField(max_length=30)

class PracticaFormulario(forms.Form):
    documento_pac = forms.IntegerField()
    fecha_practica= forms.DateField()
