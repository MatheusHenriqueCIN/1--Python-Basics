"""Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”. 
"""
# inicioCont = input("Informe se quer começar a contagem: ") # Indico se quer começar a contagem ou não.
# while (inicioCont != "Sim"): # Enquanto o input for diferente da mensagem "Sim".
#     print("Contagem Cancelada :(") # Mostra na tela essa mensagem.
#     inicioCont = input("Informe se quer começar a contagem: ") # E repete a pergunta até a palavra certa vim.
# if inicioCont == "Sim": # Se o inicio da contagem for "Sim".
#     for cont in range(10, -1 , -1): # Irá fazer um laço contador de 10 a 0
#         print(cont) # Irá printar cada número
# print("Beep") # Ira mostrar o Beep no final!!!!
# Ou use o import "winsoud apenas para o som!"

# # Seja Feliz :)

# 2 - Outra forma de realizar com o laço sem ser por "Count":
# import winsound # Adicione o Som de beep
# x = 10 # De um número a varíavel para iniciar a contagem
# while x >= 0: # Enquanto x for maior ou igual a 0
#     print(x) # Mostre o número inicial
#     x = x - 1 # Depois diminua um número e reinicie o laco
# winsound.Beep(2500, 500) # Somzinho de beep!

# # Seja feliz :)

"""Faça um programa que calcule a tabuada de um número, com valores iniciais 
e finais informados pelo usuário
"""

numberSelect = int(input("Digite o número selecionado: \n"))
begin = int(input("De o número: \n"))
end = int(input("Até o número: \n"))

x = begin
while x <= end:
    print(f"Tabuada de {numberSelect} x {x} = {numberSelect * x}")
    x += 1



    
    
    
    
    