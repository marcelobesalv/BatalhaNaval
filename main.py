from func import *
import config
import random

mapj = cria_mapa(10)
mapc = mapj
paiscj = escolher_paises(config.PAISES)
paisj = paiscj[1]
paisc = paiscj[0]
print(f'\n\nPaíses escolhidos:\nJogador: {paisj}\nComputador: {paisc}\nPosicione seus navios!\n\n')
aloca_navios(mapc,cria_lista_navios(paisc))
aloca_navios_jogador(mapj,cria_lista_navios(paisj))
print('\n\nNavios posicionados, começando jogo!\n\n')
while not foi_derrotado(mapc) or not foi_derrotado(mapj):
  ataque(mapc)
  ataque_comp(mapj)
