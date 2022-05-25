from django.shortcuts import render, HttpResponse, redirect
from .models import Jugadores, Equipos, EquiposLiga, ArquerosManager,DefensorManager, MediocampistaManager, DelanteroManager, CalendarioLiga
from .forms import EquipoForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
import random
import itertools
import sqlite3
from flask import request

# ---------------------------- VISTAS ----------------------------

def home(request):
	return render(request, "Futbol/home.html")

class nueva_partida(CreateView):
	model = EquiposLiga
	form_class = EquipoForm
	template_name = 'Futbol/nueva_partida.html'
	success_url = reverse_lazy('Menu')
 	
	def crear_liga():
		try:
			if abc=="123":
				pass
		except:
			sqlConexion=sqlite3.connect('db.sqlite3')
			cursor=sqlConexion.cursor()

			cursor.execute("SELECT nombre_equipo FROM Futbalapp_equipos ORDER BY RANDOM() LIMIT 19")
			resto_liga = cursor.fetchall()
			
			try:
				if abc=="123":
					pass
			except:
				pass
				# DESHABILITADO PARA EVITAR QUILOMBOS CON LA BBDD (!) DESPUES HABILITAR (!)

				# sql_insert = """ INSERT INTO Futbalapp_equiposliga 
				# 		(nombre_equipo, puntos_equipo, goles_favor, goles_contra)
				# 		VALUES
				# 		(?, 0, 0, 0); """
				
				# insert = cursor.executemany(sql_insert, resto_liga)
				# abc='123' 

			"""  - El ingresado mediante el formulario quedan en la posicion n° 20. (no en la ID)
			 - Su en_uso estan en True a diferencia del del resto de equipos que esta en 'False' """

			sqlConexion.commit()
			cursor.close()
			sqlConexion.close()

			return

	crear_liga()

class menu_principal(ListView):
	template_name = 'Futbol/menu_principal.html'
	context_object_name = 'formacion' # Nombre del object_list
	model = Jugadores

	"""  Generamos un queryset para el 'Model' definido en la vista """
	# def get_queryset(self):		
	# 	try:
	# 		if abc=="123":
	# 			pass
	# 	except:		
	# 		asignar_jugadores(2,7,7,6)

	# 		# Traigo los objetos declarados en el modelo
	# 		arqueros = Jugadores.arqueros_objects.all()[var1:var2]
	# 		defensores = Jugadores.defensores_objects.all()[var3:var4]
	# 		mediocampistas = Jugadores.mediocampistas_objects.all()[var5:var6]
	# 		delanteros = Jugadores.delanteros_objects.all()[var7:var8]

	# 		equipo = arqueros | defensores | mediocampistas | delanteros
	# 		abc='123'

	# 	return equipo

	
	""" Como usamos otro 'Model' pasamos el query como contexto """
	def get_context_data(self,**kwargs):
		context = super(menu_principal, self).get_context_data(**kwargs)
		context.update({
			'posiciones' : EquiposLiga.objects.order_by('puntos_equipo', 'goles_favor', 'goles_contra', 'nombre_equipo')[:5],
			'goleadores' : Jugadores.objects.order_by('goles', 'nombre')[:5],
			'equipo_propio' : EquiposLiga.objects.filter(en_uso=True),
			# Puedo seguir pasando mas contextos
		})
		return context



class competencias(ListView):
	template_name = 'Futbol/competencias.html'
	context_object_name = 'liga_completa'
	model = EquiposLiga

	def get_queryset(self,**kwargs):
		liga = EquiposLiga.objects.all().order_by('puntos_equipo', 'goles_favor', 'goles_contra', 'nombre_equipo')

		return liga


class menu_equipo(ListView):
	template_name = 'Futbol/menu_equipo.html'
	context_object_name = 'jugadores_equipo'
	model = Jugadores


	def get_queryset(self):		
		try:
			if abc=="123":
				pass
		except:		
			asignar_jugadores(2,7,7,6)

			# Traigo los objetos declarados en el modelo
			arqueros = Jugadores.arqueros_objects.all()[var1:var2]
			defensores = Jugadores.defensores_objects.all()[var3:var4]
			mediocampistas = Jugadores.mediocampistas_objects.all()[var5:var6]
			delanteros = Jugadores.delanteros_objects.all()[var7:var8]

			equipo = arqueros | defensores | mediocampistas | delanteros
			abc='123'

		return equipo


class calendario(ListView):
	template_name = 'Futbol/calendario.html'
	context = 'fixture'
	model = EquiposLiga
	
	# ARMADO DE LIGA - Desactivado para evitar quilombos
	# PD. Si quiero empezar de 0 no arranca. Entiendo que porque en 'equipos_visitantes' todavia no hay nada 
	"""try:
		if abc=="123":
			pass
	except:
		sqlConexion=sqlite3.connect('db.sqlite3')
		cursor=sqlConexion.cursor()

		cursor.execute("SELECT nombre_equipo FROM Futbalapp_equiposliga LIMIT 0,10;")
		equipos_locales = cursor.fetchall()

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 1)", equipos_locales) 

		cursor.execute("SELECT nombre_equipo FROM Futbalapp_equiposliga LIMIT 10,10;")
		equipos_visitantes = cursor.fetchall()
		sqlConexion.commit()

		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 1", equipos_visitantes[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 2", equipos_visitantes[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 3", equipos_visitantes[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 4", equipos_visitantes[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 5", equipos_visitantes[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 6", equipos_visitantes[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 7", equipos_visitantes[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 8", equipos_visitantes[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 9", equipos_visitantes[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 10", equipos_visitantes[9])
		sqlConexion.commit()

		fecha2_local = equipos_visitantes.copy()
		fecha2_local.append(equipos_locales[9])
		fecha2_local = fecha2_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 2)", fecha2_local) 
		
		fecha2_visitante = equipos_locales.copy()
		fecha2_visitante.insert(1, equipos_visitantes[0])


		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 11", fecha2_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 12", fecha2_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 13", fecha2_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 14", fecha2_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 15", fecha2_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 16", fecha2_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 17", fecha2_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 18", fecha2_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 19", fecha2_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 20", fecha2_visitante[9])

		fecha3_local = fecha2_visitante.copy()
		fecha3_local.insert(1, fecha2_local[0])
		fecha3_local = fecha3_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 3)", fecha3_local)


		fecha3_visitante = fecha2_local.copy()
		fecha3_visitante.append(fecha2_visitante[9])
		fecha3_visitante = fecha3_visitante[1:11]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 21", fecha3_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 22", fecha3_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 23", fecha3_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 24", fecha3_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 25", fecha3_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 26", fecha3_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 27", fecha3_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 28", fecha3_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 29", fecha3_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 30", fecha3_visitante[9])

		fecha4_local = fecha3_visitante.copy()
		fecha4_local.append(fecha3_local[9])
		fecha4_local = fecha4_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 4)", fecha4_local) 
		
		fecha4_visitante = fecha3_local.copy()
		fecha4_visitante.insert(1, fecha3_visitante[0])
		fecha4_visitante = fecha4_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 31", fecha4_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 32", fecha4_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 33", fecha4_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 34", fecha4_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 35", fecha4_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 36", fecha4_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 37", fecha4_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 38", fecha4_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 39", fecha4_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 40", fecha4_visitante[9])

		fecha5_local = fecha4_visitante.copy()
		fecha5_local.insert(1, fecha4_local[0])
		fecha5_local = fecha5_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 5)", fecha5_local) 
		
		fecha5_visitante = fecha4_local.copy()
		fecha5_visitante.append(fecha4_visitante[9])
		fecha5_visitante = fecha5_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 41", fecha5_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 42", fecha5_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 43", fecha5_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 44", fecha5_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 45", fecha5_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 46", fecha5_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 47", fecha5_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 48", fecha5_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 49", fecha5_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 50", fecha5_visitante[9])

		fecha6_local = fecha5_visitante.copy()
		fecha6_local.append(fecha5_local[9])
		fecha6_local = fecha6_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 6)", fecha6_local) 
		
		fecha6_visitante = fecha5_local.copy()
		fecha6_visitante.insert(1, fecha5_visitante[0])
		fecha6_visitante = fecha6_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 51", fecha6_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 52", fecha6_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 53", fecha6_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 54", fecha6_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 55", fecha6_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 56", fecha6_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 57", fecha6_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 58", fecha6_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 59", fecha6_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 60", fecha6_visitante[9])	

		fecha7_local = fecha6_visitante.copy()
		fecha7_local.insert(1, fecha6_local[0])
		fecha7_local = fecha7_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 7)", fecha7_local) 
		
		fecha7_visitante = fecha6_local.copy()
		fecha7_visitante.append(fecha6_visitante[9])
		fecha7_visitante = fecha7_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 61", fecha7_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 62", fecha7_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 63", fecha7_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 64", fecha7_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 65", fecha7_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 66", fecha7_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 67", fecha7_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 68", fecha7_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 69", fecha7_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 70", fecha7_visitante[9])

		fecha8_local = fecha7_visitante.copy()
		fecha8_local.append(fecha7_local[9])
		fecha8_local = fecha8_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 8)", fecha8_local) 
		
		fecha8_visitante = fecha7_local.copy()
		fecha8_visitante.insert(1, fecha7_visitante[0])
		fecha8_visitante = fecha8_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 71", fecha8_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 72", fecha8_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 73", fecha8_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 74", fecha8_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 75", fecha8_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 76", fecha8_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 77", fecha8_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 78", fecha8_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 79", fecha8_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 80", fecha8_visitante[9])	

		fecha9_local = fecha8_visitante.copy()
		fecha9_local.insert(1, fecha8_local[0])
		fecha9_local = fecha9_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 9)", fecha9_local) 
		
		fecha9_visitante = fecha8_local.copy()
		fecha9_visitante.append(fecha8_visitante[9])
		fecha9_visitante = fecha9_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 81", fecha9_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 82", fecha9_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 83", fecha9_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 84", fecha9_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 85", fecha9_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 86", fecha9_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 87", fecha9_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 88", fecha9_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 89", fecha9_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 90", fecha9_visitante[9])

		fecha10_local = fecha9_visitante.copy()
		fecha10_local.append(fecha9_local[9])
		fecha10_local = fecha10_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 10)", fecha10_local) 
		
		fecha10_visitante = fecha9_local.copy()
		fecha10_visitante.insert(1, fecha9_visitante[0])
		fecha10_visitante = fecha10_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 91", fecha10_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 92", fecha10_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 93", fecha10_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 94", fecha10_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 95", fecha10_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 96", fecha10_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 97", fecha10_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 98", fecha10_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 99", fecha10_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 100", fecha10_visitante[9])	

		fecha11_local = fecha10_visitante.copy()
		fecha11_local.insert(1, fecha10_local[0])
		fecha11_local = fecha11_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 11)", fecha11_local) 
		
		fecha11_visitante = fecha10_local.copy()
		fecha11_visitante.append(fecha10_visitante[9])
		fecha11_visitante = fecha11_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 101", fecha11_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 102", fecha11_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 103", fecha11_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 104", fecha11_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 105", fecha11_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 106", fecha11_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 107", fecha11_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 108", fecha11_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 109", fecha11_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 110", fecha11_visitante[9])

		fecha12_local = fecha11_visitante.copy()
		fecha12_local.append(fecha11_local[9])
		fecha12_local = fecha12_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 12)", fecha12_local) 
		
		fecha12_visitante = fecha11_local.copy()
		fecha12_visitante.insert(1, fecha11_visitante[0])
		fecha12_visitante = fecha12_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 111", fecha12_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 112", fecha12_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 113", fecha12_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 114", fecha12_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 115", fecha12_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 116", fecha12_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 117", fecha12_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 118", fecha12_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 119", fecha12_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 120", fecha12_visitante[9])	
		
		fecha13_local = fecha12_visitante.copy()
		fecha13_local.insert(1, fecha12_local[0])
		fecha13_local = fecha13_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 13)", fecha13_local) 
		
		fecha13_visitante = fecha12_local.copy()
		fecha13_visitante.append(fecha12_visitante[9])
		fecha13_visitante = fecha13_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 121", fecha13_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 122", fecha13_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 123", fecha13_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 124", fecha13_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 125", fecha13_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 126", fecha13_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 127", fecha13_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 128", fecha13_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 129", fecha13_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 130", fecha13_visitante[9])

		fecha14_local = fecha13_visitante.copy()
		fecha14_local.append(fecha13_local[9])
		fecha14_local = fecha14_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 14)", fecha14_local) 
		
		fecha14_visitante = fecha13_local.copy()
		fecha14_visitante.insert(1, fecha13_visitante[0])
		fecha14_visitante = fecha14_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 131", fecha14_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 132", fecha14_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 133", fecha14_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 134", fecha14_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 135", fecha14_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 136", fecha14_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 137", fecha14_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 138", fecha14_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 139", fecha14_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 140", fecha14_visitante[9])		

		fecha15_local = fecha14_visitante.copy()
		fecha15_local.insert(1, fecha14_local[0])
		fecha15_local = fecha15_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 15)", fecha15_local) 
		
		fecha15_visitante = fecha14_local.copy()
		fecha15_visitante.append(fecha14_visitante[9])
		fecha15_visitante = fecha15_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 141", fecha15_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 142", fecha15_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 143", fecha15_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 144", fecha15_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 145", fecha15_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 146", fecha15_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 147", fecha15_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 148", fecha15_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 149", fecha15_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 150", fecha15_visitante[9])

		fecha16_local = fecha15_visitante.copy()
		fecha16_local.append(fecha15_local[9])
		fecha16_local = fecha16_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 16)", fecha16_local) 
		
		fecha16_visitante = fecha15_local.copy()
		fecha16_visitante.insert(1, fecha15_visitante[0])
		fecha16_visitante = fecha16_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 151", fecha16_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 152", fecha16_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 153", fecha16_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 154", fecha16_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 155", fecha16_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 156", fecha16_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 157", fecha16_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 158", fecha16_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 159", fecha16_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 160", fecha16_visitante[9])

		fecha17_local = fecha16_visitante.copy()
		fecha17_local.insert(1, fecha16_local[0])
		fecha17_local = fecha17_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 17)", fecha17_local) 
		
		fecha17_visitante = fecha16_local.copy()
		fecha17_visitante.append(fecha16_visitante[9])
		fecha17_visitante = fecha17_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 161", fecha17_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 162", fecha17_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 163", fecha17_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 164", fecha17_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 165", fecha17_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 166", fecha17_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 167", fecha17_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 168", fecha17_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 169", fecha17_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 170", fecha17_visitante[9])

		fecha18_local = fecha17_visitante.copy()
		fecha18_local.append(fecha17_local[9])
		fecha18_local = fecha18_local[1:11]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 18)", fecha18_local) 
		
		fecha18_visitante = fecha17_local.copy()
		fecha18_visitante.insert(1, fecha17_visitante[0])
		fecha18_visitante = fecha18_visitante[0:10]

		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 171", fecha18_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 172", fecha18_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 173", fecha18_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 174", fecha18_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 175", fecha18_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 176", fecha18_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 177", fecha18_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 178", fecha18_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 179", fecha18_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 180", fecha18_visitante[9])

		fecha19_local = fecha18_visitante.copy()
		fecha19_local.insert(1, fecha18_local[0])
		fecha19_local = fecha19_local[0:10]

		cursor.executemany("INSERT INTO Futbalapp_calendarioliga (equipo_local, equipo_visitante, fecha) VALUES (?, 1, 19)", fecha19_local) 
		
		fecha19_visitante = fecha18_local.copy()
		fecha19_visitante.append(fecha18_visitante[9])
		fecha19_visitante = fecha19_visitante[1:11]
		
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 181", fecha19_visitante[0])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 182", fecha19_visitante[1])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 183", fecha19_visitante[2])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 184", fecha19_visitante[3])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 185", fecha19_visitante[4])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 186", fecha19_visitante[5])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 187", fecha19_visitante[6])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 188", fecha19_visitante[7])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 189", fecha19_visitante[8])
		cursor.execute("UPDATE Futbalapp_calendarioliga SET equipo_visitante = (?) WHERE posicion_tabla = 190", fecha19_visitante[9])

		sqlConexion.commit()
		cursor.close()
		sqlConexion.close()

		abc='123'"""

	def get_context_data(self,**kwargs):
		context = super(calendario, self).get_context_data(**kwargs)
		context.update({
			'fecha' : CalendarioLiga.objects.filter(fecha=1),
		})
		return context

def calendario_filtrado(request, fecha):
	calendario_por_fecha=CalendarioLiga.objects.filter(fecha=fecha)
	return render(request, 'Futbol/calendario.html', {"fecha":calendario_por_fecha})

	# Me funciona para hacer el calendario interactivo pero tengo que ver donde meter el 'armado de liga'

# ---------------------------- EJECUTAR UNA SOLA VEZ ----------------------------

def ejecucion_unica(funcion_parametro):
    
    def funcion_interior(*args):
        if not funcion_interior.has_run:
            funcion_interior.has_run = True
            return funcion_parametro(*args)
    
    funcion_interior.has_run = False
    return funcion_interior

@ejecucion_unica
def asignar_jugadores(gk_var, df_var, mc_var, dc_var):
	global var1
	global var2
	global var3
	global var4
	global var5
	global var6
	global var7
	global var8

	var1=random.randrange(1,6)
	var2=var1 + gk_var

	var3=random.randrange(1,6)
	var4=var3 + df_var

	var5=random.randrange(1,6)
	var6=var5 + mc_var

	var7=random.randrange(1,6)
	var8=var7 + dc_var



""" COSAS A CORREGIR:
	- Al iniciar de 0 la base de datos no tiene cargado a los jugadores y a los equipos (necesario para que funcione)
	- Al iniciar, no deja hacerlo con el codigo completo ya que en varias ocasiones llamo a 'tablas' que aun no estan declaradas
	- La creacion de la liga se vuelve a ejecutar si vuelvo a inciar el servidor (Puede que sea correcto que haga esto) 


"""