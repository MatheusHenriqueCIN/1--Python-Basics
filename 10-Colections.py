# # É possível criar uma list em um proprío negócio

gameFifa = ["Fifa 23", 2022, 120.50, True]
print(gameFifa)

# Não necessariamente precisa tudo igual
gamesList = ["Red Dead Redemption","Star Wars Jedi",
             "Fifa 25","Dark Souls 3","Mario Odyssey"]

print(gamesList)

# 1 - Buscar os dois primeiros itens da Lista | [0:-1]
print(gamesList[0:2])

# 2 - Buscar o ultimo item da lista | -1
print(gamesList[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesList[:3])

# 4 - Buscar jogos de uma posição em diante | -1 no ultimo então para pegar o 4 jogo tem que ser 4-1 = 3 já que o primeiro é 0
print(gamesList[1:4])