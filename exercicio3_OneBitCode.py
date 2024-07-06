# Primeiro exercício para utilização de if, elif e else.

"""" Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.
"""
# 1 - Primeiro pegamos a distância que a pessoa ira percorrer.

dist = float(input("Digite a distância que ira percorrer: "))

# 2 - Adicionamos a variável se for < ou = a 200

if dist <= 200:
    preco = 0.5 * dist
# 3 - Adicionamos agora a variavel se não for nenhuma da condição acima.

else:
    preco = 0.35 * dist
# 4 - Printamos na tela o valor da passagem da pessoa.   

print(f"O preço da sua passagem será de {preco:.2f} reais.")

# Seja feliz :)

# Segundo exercício para utilização de if, elif e else.

""" Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""

# 1 - Primeiro perguntamos o valor do salário da pessoa em formato String (Já que é um salário).

salario = float(input("Digite o valor do seu salário: "))

# 2 - Adicionamos o aumento do valor do salário caso seja acima de 1250R$.

if salario > 1250.00:
    novoSalario = salario * 1.1
    
# 3 - Adicionamos agora caso seja igual ou menor que o salário de 1250R$.

else:
    novoSalario = salario * 1.15
    
# 4 - Printamos na tela o novo salário da pessoa.
print(f"O seu novo salário sera de: {novoSalario:.2f}")

# Seja feliz :)
      
