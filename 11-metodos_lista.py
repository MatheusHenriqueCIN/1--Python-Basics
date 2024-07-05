
# # Coisas para utilizar em uma lista.


gamesList = ["Red Dead Redemption","Star Wars Jedi",
             "Fifa 25","Dark Souls 3","Mario Odyssey","Mario"]

# 1 - Tamanho da Lista | (len) = Lenght = Quantidade de elementos
print(len(gamesList))

# 2 - Recuperar um item da lista pelo índice (index)
print(gamesList.index("Fifa 25"))

# 3 - Adicionar item ao final da lista (append)
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordenar a lista de maiusculo para minúsculo (sort)
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra (copy) e remove um elemento(remove) | gameReset = jogos que eu ja zerei
gameReset = gamesList.copy()
gameReset.remove("Star Wars Jedi")
print(gameReset)

# 6 - Remove todos os itens da Lista (clear)
gamesList.clear()
print(gamesList)