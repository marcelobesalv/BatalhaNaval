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
