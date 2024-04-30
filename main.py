from func import *
import config
import random
tmap = int(input('Tamanho do mapa: '))
mapj = cria_mapa(tmap)
mapc = mapj
paiscj = escolher_paises(config.PAISES)
paisj = paiscj[1]
paisc = paiscj[0]
aloca_navios(mapc,cria_lista_navios(paisc))
aloca_navios_jogador(mapj,cria_lista_navios(paisj))
while not foi_derrotado(mapc) or not foi_derrotado(mapj):
  ataque(mapc)
  ataque_comp(mapj)


