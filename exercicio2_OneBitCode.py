""" Pergunta 1: O primeiro desafio consiste em escrever um código que recebe o 
nome de um jogo digitado pelo usuário, verifica se há algum caractere 
repetido e substitui a segunda ocorrência desse caractere por um símbolo, 
no caso o cifrão ($).
"""

# # Adicione a Frase
frase = (input("Digite sua frase "))

# # Pegue a primeira Letra da String
firstLetter = (frase[0:1])

# # Pegue o resto da string
frase2 = (frase[1:])

# # Substitua o resto da string pelo caractere $ igual a primeira letra da String
frase3 = (frase2.replace(firstLetter,"$"))

# # Deixe a primeira letra na String em Maiúsculo
(firstLetter.upper())

# # Adicione a primeira letra no resto da String
Frase4 = firstLetter + frase3
# # Print Ela
print(Frase4)

# # Seja feliz :)


""" Pergunta 2: O segundo desafio envolve trocar os 
dois primeiros caracteres de duas strings diferentes.
O objetivo é inverter os dois primeiros caracteres
"""

# Adicione as duas frases
frase1 = (input("Digite sua primeira frase: "))
frase2 = (input("Digite sua segunda frase: "))

# Pegue a quantidade de caracteres da primeira string e a da segunda
quantCaract1 = (len(frase1))
quantCaract1 = quantCaract1 - 1
quantCaract2 = (len(frase2))
quantCaract2 = quantCaract2 - 1

#Pegue a letra do ultimo caractere
total1 = (frase1[quantCaract1:])
total2 = (frase2[quantCaract2:])

#Substitua uma letra em cada String
totalGeral1 = (frase1.replace(total1,total2))
totalGeral2 = (frase2.replace(total2,total1))

# Some as duas com espaço entre elas
totalTudal = totalGeral1 + " " + totalGeral2

# Print ela
print(totalTudal)

#Seja Feliz :)



