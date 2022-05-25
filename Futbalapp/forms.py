# Podemos crear contenido html basado en un modelo

from django import forms
from .models import EquiposLiga, CalendarioLiga


class EquipoForm(forms.ModelForm):
	class Meta:
		model = EquiposLiga
		fields = ('nombre_equipo',)
		# fields = ('nombre', 'apellido',)