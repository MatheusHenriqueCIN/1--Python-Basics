gamesTuple = ("Fifa 23","Red dead 2",
             "Legend of Zelda","Mario Odyssey")
print(gamesTuple)
print(type(gamesTuple))
# name = ("Rodrigo") #Se eu tenho um nome sem uma virgula pós parentese = str / Com virgula = tupla
# print(type(name))

# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o ultimos itens da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição | 3 elementos
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[1:])

# 5 - Recuperaer um item da tupla pelo índice
print(gamesTuple.index("Legend of Zelda"))

