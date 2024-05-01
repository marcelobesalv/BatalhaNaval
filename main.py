from func import *
import config
import random
jogar = True
continuar = ''
while jogar:
  mapj = cria_mapa(10)
  mapc = cria_mapa(10)
  paiscj = escolher_paises(config.PAISES)
  paisj = paiscj[1]
  paisc = paiscj[0]
  print(f'\n\nPaíses escolhidos:\nJogador: {paisj}\nComputador: {paisc}\nPosicione seus navios!\n\n')
  aloca_navios(mapc,cria_lista_navios(paisc))
  aloca_navios_jogador(mapj,cria_lista_navios(paisj))
  print('\n\nNavios posicionados, começando jogo!\n\n')
  while not foi_derrotado(mapc) and not foi_derrotado(mapj):
    ataque(mapc)
    ataque_comp(mapj)
  if foi_derrotado(mapc):
    print('Você ganhou')
  else:
    print('Você perdeu')
  while True:
    contiuar = input('Quer jogar mais uma vez? \n', '(Sim/Não)').lower()
    if continuar != 'sim' and continuar != 'nâo' and continuar != 'nao':
      continue
    elif continuar == 'sim':
      break
    elif continuar == 'nao' or continuar == 'não':
      jogar = False
      break
    
    
