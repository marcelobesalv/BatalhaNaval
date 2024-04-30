def cria_mapa(n):
    return [[' ']*n for i in range(n)]

def foi_derrotado(m):
    for i in m: 
        if 'N' in i: return False
    return True
