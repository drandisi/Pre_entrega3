from django import forms

class Bomberoformulario(forms.Forms):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    cargo = forms.CharField(max_length=40)
    numero = forms.CharField(max_length=20)
    division = forms.CharField(max_length=40)

class divisionformulario(forms.Forms):
    nombre_division = forms.CharField(max_length=40)
    encargados_division = forms.CharField(max_length=40)


class guardiaformulario(forms.Forms):
    
    dia = forms.CharField(max_length=40)
    encargado_guardia = forms.CharField(max_length=40)