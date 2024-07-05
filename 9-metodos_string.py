gameName = "Fifa 24"
gameDescription = """
     Fifa 24 é um jogo de futebol,
     desenvolvido pela EA Sports, que Possibilita 
     jogar localmente ou online
"""

print(gameName.upper()) # Retornar string em maiúsculo
print(gameName.lower()) # Retornar string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em minúsculo
print(gameName.title()) # Apenas a primeira Letra em Maiúsculo
print(gameName.center(11, '-')) # Retorna a String centralizada com preenchimento
print(gameName.find("a")) # Retorna a posição de um determinado caractere
print(gameDescription.count("f")) # Conta Caracteres
print(gameName.count("a")) # Conta Caracteres
print(gameDescription.replace("Fifa","Pes")) # Altera um elemento pelo outro
print(gameDescription.split(",")) # Consegue eliminar um elemento de uma string