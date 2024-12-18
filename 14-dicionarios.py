# Como utilizar um dicionario
# É possivel adicionar uma lista dentro de um dicionário

gameFifa = {
    "name": "Fifa 23",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["esporte", "familia"]

}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get("classification"))

# 2 - Buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Buscar apenas as chaves do dicionário
print(gameFifa.values())

# 4 - Buscar itens do dicionário com chave e valor
print(gameFifa.items())

# 5 - Adicionar itens no dicionário
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizar os itens no dicionário
gameFifa.update({"players":1})

# 7 - Remover itens no dicionário
gameFifa.pop("players")
print(gameFifa)