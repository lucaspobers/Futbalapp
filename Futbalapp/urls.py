from django.urls import path, include
from Futbalapp.views import home, menu_principal, nueva_partida, competencias, calendario, menu_equipo, calendario_filtrado

extrapatterns = [
    path('', menu_principal.as_view(), name='Menu'),
    path('competencias/', competencias.as_view(), name='Competencias'),
    path('calendario/1/', calendario.as_view(), name='Calendario'),
    path('calendario/<int:fecha>/', calendario_filtrado, name='Calendario'),
    path('equipo/', menu_equipo.as_view(), name='Equipo'),

]


urlpatterns = [
    path('', home, name='Home'),
    path('start/', nueva_partida.as_view(), name='Nueva Partida'),
    path('menu/', include(extrapatterns)),
 ]

