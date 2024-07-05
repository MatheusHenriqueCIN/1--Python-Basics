# Como adicionar um dicionário dentro do outro
import pprint
gamesDict = {
    "Resident Evil 4": {
        "yearLaunch":2023,
        "Classification": 9.8,
        "genre": ["ação","aventura"]
    },
    "Mario Odyssey": {
        "yearLaunch":2017,
        "Classification":9.5,
        "genre": ["3d","aventura"]
        },
    "Elden Ring": {
        "yearLaunch": 2022,
        "Classification": 10,
        "genre": ["ação,","história"]
    }
    
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionario
print(gamesDict["Mario Odyssey"]["genre"])

# 2 - Adicionar novos itens
gamesDict["Mario Odyssey"]["players"] = 1
print(gamesDict["Mario Odyssey"])

# 3 - Excluir um dicionário
del gamesDict["Resident Evil 4"]
pp.pprint(gamesDict)