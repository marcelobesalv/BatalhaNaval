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
    for i in ln:
        l = random.randint(0, i-1)
        c = random.randint(0, i-1)
        o = random.choice(['h', 'v'])
        while not(posicao_suporta(m, i, l, c, o)):
            l = random.randint(0, i-1)
            c = random.randint(0, i-1)
            o = random.choice(['h', 'v'])
        for j in range(i):
            if o == 'v':
                m[l+j][c] = 'N'
            else: m[l][c+j] = 'N'
    return m
    
def foi_derrotado(m):
    for i in m: 
        if 'N' in i: return False
    return True

def escolher_paises(PAISES):
    
    while True:
        nacaoj = input('Nação: ')
        if nacaoj in PAISES:
            break
    while True:
        nacaoc = random.choice(list(PAISES.keys()))
        if nacaoc != nacaoj:
            break
    return [PAISES[nacaoc],PAISES[nacaoj]]


def cria_lista_navios(pais):
    ln = []
    for tipo, qnt in PAISES[pais].items():
        for i in range(qnt):
            ln.append(CONFIGURACAO[tipo])
    return ln

def ataque(m):
    while True:
        print(m)
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
                print('fogo')
                m[y][x] = 'F'
                return m
            elif m[y][x] == ' ':
                print('agua')
                m[y][x] = 'A'
                return m
            else: print('Ataque inválido')
