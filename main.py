from func.py import *
tmap = int(input('Tamanho do mapa: '))
mapj = cria_mapa(tmap)
mapc = mapj
paisj = escolher_paises(PAISES)[1]
paisc = escolher_paises(PAISES)[0]
aloca_navios(mapc,cria_lista_navios(paisc))
aloca_navios_jogador(mapj,cria_lista_navios(paisj))
while not foi_derrotado(mapc) or not foi_derrotado(mapj):
  ataque(mapc)
  ataque_comp(mapj)


