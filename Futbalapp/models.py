from django.db import models

""" ---------------- MODELS MANAGERS ----------------
Los uso para organizar mejor la BBDD. Ya tengo 'prefiltrado' en una variable cada jugador por posicion """


class ArquerosManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(posicion='Arquero')

class DefensorManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(posicion='Defensor')

class MediocampistaManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(posicion='Mediocampista')

class DelanteroManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(posicion='Delantero')


# ---------------- MODELS / TABLAS ----------------

class Jugadores(models.Model):

	def __str__(self):
		return f"{self.nombre} {self.apellido} {self.posicion} {self.pais} Valoracion: {self.valoracion}"

	paises = (
		('AR', 'Argentina'),
		('BR', 'Brasil'),
		('UR', 'Uruguay'),
		('PE', 'Peru'),
		('CO', 'Colombia'),
		('PA', 'Paraguay'),
		('CH', 'Chile'),
		('EC', 'Ecuador'),
		('BO', 'Bolivia'),
		('VE', 'Venezuela'),
	)

	posiciones = (
		('Arquero', 'Arquero'),
		('Defensor', 'Defensor'),
		('Mediocampista', 'Mediocampista'),
		('Delantero', 'Delantero'),
	)

	nombre=models.CharField(max_length=15, verbose_name="Nombre")
	apellido=models.CharField(max_length=25, verbose_name="Apellido")
	pais=models.CharField(max_length=15, choices=paises, verbose_name="Pais")
	valoracion=models.IntegerField(verbose_name="Valoracion", blank=True, null=True)
	posicion=models.CharField(max_length=15, choices=posiciones, verbose_name='Posicion', blank=True, null=True)
	goles=models.IntegerField(verbose_name="Goles", default=0)
	velocidad=models.IntegerField(verbose_name="Velocidad", blank=True, null=True)
	regate=models.IntegerField(verbose_name="Regate", blank=True, null=True)
	pase=models.IntegerField(verbose_name="Pase", blank=True, null=True)
	tiro=models.IntegerField(verbose_name="Tiro", blank=True, null=True)
	defensa=models.IntegerField(verbose_name="Defensa", blank=True, null=True)
	fisico=models.IntegerField(verbose_name="Fisico", blank=True, null=True)
	goles=models.IntegerField(verbose_name="Goles", default=0)
	# en_uso=models.BooleanField()

	objects = models.Manager()
	
	arqueros_objects = ArquerosManager()
	defensores_objects = DefensorManager()
	mediocampistas_objects = MediocampistaManager()
	delanteros_objects = DelanteroManager()


class Equipos(models.Model):
	def __str__(self):
		return f"{self.nombre_equipo}"

	nombre_equipo=models.CharField(max_length=15, verbose_name="Nombre Equipo")
	puntos_equipo=models.IntegerField(default=0, verbose_name="Puntos")
	goles_favor=models.IntegerField(default=0, verbose_name="Goles a Favor")
	goles_contra=models.IntegerField(default=0, verbose_name="Goles en Contra")

	# jugadores_equipo=models.ManyToManyField(Jugadores)
	

class EquiposLiga(models.Model):
	# def __str__(self):
	# 	return f'{self}'

	nombre_equipo=models.CharField(max_length=25, verbose_name="Nombre Equipo")
	puntos_equipo=models.IntegerField(default=0, verbose_name="Puntos", blank=True, null=True)
	goles_favor=models.IntegerField(default=0, verbose_name="Goles a Favor", blank=True, null=True)
	goles_contra=models.IntegerField(default=0, verbose_name="Goles en Contra", blank=True, null=True)
	partidos_jugados=models.IntegerField(default=0, verbose_name="Partidos Jugados", blank=True, null=True)
	partidos_ganados=models.IntegerField(default=0, verbose_name="Partidos Ganados", blank=True, null=True)
	partidos_empatados=models.IntegerField(default=0, verbose_name="Partido Empatados", blank=True, null=True)
	partidos_perdidos=models.IntegerField(default=0, verbose_name="Partidos Perdidos", blank=True, null=True)
	en_uso=models.BooleanField(default=True, null=True)


class CalendarioLiga(models.Model):

	posicion_tabla=models.AutoField(verbose_name="Posicion Tabla", primary_key=True)
	fecha=models.IntegerField(verbose_name="Fecha", blank=True, null=True)
	equipo_local=models.CharField(max_length=25, verbose_name="Equipo Local")
	goles_local=models.IntegerField(default=0, verbose_name="Goles Local", blank=True, null=True)
	goles_visitante=models.IntegerField(default=0, verbose_name="Goles Visitante", blank=True, null=True)
	equipo_visitante=models.CharField(max_length=25, verbose_name="Equipo Visitante")


# class PlantelPropio(models.Model):

# 	nombre=models.CharField(max_length=15, verbose_name="Nombre")
# 	apellido=models.CharField(max_length=25, verbose_name="Apellido")
# 	velocidad=models.IntegerField(verbose_name="Velocidad")
# 	regate=models.IntegerField(verbose_name="Regate")
# 	pase=models.IntegerField(verbose_name="Pase")
# 	tiro=models.IntegerField(verbose_name="Tiro")
# 	defensa=models.IntegerField(verbose_name="Defensa")
# 	fisico=models.IntegerField(verbose_name="Fisico")
# 	valoracion=models.IntegerField(verbose_name="Valoracion")
# 	posicion=models.CharField(max_length=15, verbose_name='Posicion', blank=True, null=True)
# 	goles=models.IntegerField(verbose_name="Goles", default=0)	
# 	pais=models.CharField(max_length=15, verbose_name="Pais")