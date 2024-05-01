import random
from config import *
from copy import deepcopy
def cria_mapa(n):
    return [[' ']*n for i in range(n)]

def posicao_suporta(m, t, l, c, o):
    if o == 'v': 
        if l+t > len(m): return False
        for i in range(t):
            if m[l+i][c] != ' ': return False
    else: 
        if c+t > len(m): return False
        for i in range(t):
            if m[l][c+i] != ' ': return False
    return True

def aloca_navios(m, ln):
    counter, i = 0, 0
    while i < len(ln):
        print('a')
        l = random.randint(0, len(m)-ln[i])
        c = random.randint(0, len(m)-ln[i])
        o = random.choice(['h', 'v'])
        while not(posicao_suporta(m, ln[i], l, c, o)):
            print('b')
            l = random.randint(0, len(m)-ln[i])
            c = random.randint(0, len(m)-ln[i])
            o = random.choice(['h', 'v'])
            counter += 1
            if counter > 100:
                i = 0
                break
        if posicao_suporta(m, ln[i], l, c, o):  
            for j in range(ln[i]):
                if o == 'v':
                    m[l+j][c] = 'N'
                else: m[l][c+j] = 'N'
            i += 1
    return m
    
def foi_derrotado(m):
    for i in m: 
        if 'N' in i: return False
    return True

def escolher_paises(PAISES):
    print('Escolha uma das seguintes nações: Brasil, França, Austrália, Rússia, Japão')
    while True:
        nacaoj = input('Nação: ').capitalize()
        if nacaoj in PAISES:
            break
        else: print('Nação inválida')
    while True:
        nacaoc = random.choice(list(PAISES.keys()))
        if nacaoc != nacaoj:
            break
    return [nacaoc,nacaoj]


def cria_lista_navios(pais):
    ln = []
    for tipo, qnt in PAISES[pais].items():
        for i in range(qnt):
            ln.append(CONFIGURACAO[tipo])
    return ln
    
def ataque_comp(m):
    y = random.randint(0, len(m)-1)
    x = random.randint(0, len(m)-1)
    if m[y][x] == 'N':
        print('Computador: fogo!')
        m[y][x] = 'F'
        return m
    elif m[y][x] == ' ':
        print('Computador: água!')
        m[y][x] = 'A'
        return m
        
def ataque(m):
    while True:
        mc = deepcopy(m)
        print('m:')
        for i in m:
            print(i)
        print('mc:')
        for i in range(len(mc)):
            for j in range(len(mc[i])):
                if mc[i][j] == 'N':
                    mc[i][j] = ' '
            print(mc[i])
        erro = 0
        x = input('Letra: ').upper()
        if x not in ALFABETO or ALFABETO.index(x) > len(m)-1:
            print('Letra inválida')
            erro += 1   
        if not(erro):
            y = input('Número: ')
            if not(y.isdigit()) or int(y) > len(m[0]): 
                print('Numero inválido')
                erro += 1
        if not(erro):
            x = ALFABETO.index(x)
            y = int(y)
            y -= 1
            print(ALFABETO[x], str(y+1))
            if m[y][x] == 'N':
                print('Jogador: fogo!')
                m[y][x] = 'F'
                return m
            elif m[y][x] == ' ':
                print('Jogador: água!')
                m[y][x] = 'A'
                return m
            else: print('Ataque inválido')
                
def aloca_navios_jogador(m,ln):
    for linha in m:
            print(linha)
    for i in ln:
        l = len(m)+1
        c = len(m)+1
        o = 'v'
        n = 0 
        while not(posicao_suporta(m, i, c, l, o)):
            print('Tamanho do navio:',i)
            if n >=1:
                print('posicao invalida')
            l = input('Letra: ').upper()
            while l not in ALFABETO or ALFABETO.index(l) > len(m)-1 or l =='':
                print('Letra inválida')
                l = input('Letra: ').upper()
                 
            c = input('Número: ')
            while not(c.isdigit()) or int(c) > len(m[0]):
                     
                print('Número inválido')
                c = input('Número: ')

            o = input('Orientação (h/v): ')
            while o!='h' and o!='v':
                print('Opção inválida')
                o = input('Orientação (h/v): ')
            
            l = ALFABETO.index(l)
            c = int(c)
            c -= 1
            n+=1 
        for j in range(i):
            if o == 'v':
                m[c+j][l] = 'N'
            else: m[c][l+j] = 'N'
        for linha in m:
            print(linha)
    return m
