#Utilizar tipos de dado Set

gamesSet = {"Fifa 23", "Legend of Zelda", "Star Wars", "Mario Odyssey", "Resident Evil 4"}
print(gamesSet)

# - Mão possibilita recuperar valores via fatiamento ou slice

# 1 - Buscar tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados os mesmo valores
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)
