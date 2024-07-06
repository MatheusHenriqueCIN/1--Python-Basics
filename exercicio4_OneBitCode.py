"""Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”. 
"""
inicioCont = input("Informe se quer começar a contagem: ") # Indico se quer começar a contagem ou não.
while (inicioCont != "Sim"): # Enquanto o input for diferente da mensagem "Sim".
    print("Contagem Cancelada :(") # Mostra na tela essa mensagem.
    inicioCont = input("Informe se quer começar a contagem: ") # E repete a pergunta até a palavra certa vim.
if inicioCont == "Sim": # Se o inicio da contagem for "Sim".
    for cont in range(10, -1 , -1): # Irá fazer um laço contador de 10 a 0
        print(cont) # Irá printar cada número
print("Beep") # Ira mostrar o Beep no final!!!!
# Ou use o import "winsoud apenas para o som!"

# # Seja Feliz :)

# 2 - Outra forma de realizar com o laço sem ser por "Count":
import winsound # Adicione o Som de beep
x = 10 # De um número a varíavel para iniciar a contagem
while x >= 0: # Enquanto x for maior ou igual a 0
    print(x) # Mostre o número inicial
    x = x - 1 # Depois diminua um número e reinicie o laco
# winsound.Beep(2500, 500) # Somzinho de beep!

# # Seja feliz :)

"""Faça um programa que calcule a tabuada de um número, com valores iniciais 
e finais informados pelo usuário
"""

numberSelect = int(input("Digite o número selecionado: \n"))  # Aqui a pessoa diz qual número selecionou.
begin = int(input("De o número: \n")) # Aqui diz de qual número começa seja até de 0.
end = int(input("Até o número: \n")) # Aqui diz até qual número vai multiplicar.
 
x = begin # A váriavel x irá pegar o número inicial para começar o laço.
while x <= end: # "Enquanto o número inicial for menor que o número final".
    print(f"Tabuada de {numberSelect} x {x} = {numberSelect * x}") # Mostre na tela a multiplicação.
    x += 1 # Aqui concatene +1 para continuar o laço até o número que deseja mostrar.

# # Seja feliz :)
    



    
    
    
    
    
