gameName = "Fifa 24"
gameDescription = """
     Fifa 24 é um jogo de futebol
     desenvolvido pela EA Sports que Possibilita 
     jogar localmente ou online
"""

# string[inicio:fim] - índice começa na posição 0 | índice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string a partir da ultima posição
print(gameName[:5])

# 3 - Busque toda string da terceira até a ultima posição
print(gameName[2:])

"""
# string[inicio:fim:passo] - índice começa na posição 0 | índice final -1
passso - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string no índices ímapres
print(gameName[1::2])

# 6 - Inverter uma String
print(gameName[::-1])