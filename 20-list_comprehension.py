# 1 - Liste valores de 0 a 10 que sejam menores do que 4.
# for i in range(10):
#     if i < 4:          # Da pra fazer isso por for tranquilamente.
#         print(i)

listNumber = [i for i in range(10) if i < 4]
print(listNumber) # Retorna em uma lista, apenas com uma linha de código faz o mesmo de cima.


gamesList = ["Fifa", "God of War", 
            "Red Dead 2", "Uncharted","Kirby"]

# 2 - Jogos que possuem a Letra A.
newList = [x for x in gamesList if "a" in x]
print(newList)

# 3 - Jogos que eu zerei para eu retirar.
gamesFinished = [x for x in gamesList if x != "Kirby"]
print(gamesFinished)