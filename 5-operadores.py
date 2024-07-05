num1 = int(input("Digite o primeiro numero\n"))
num2 = int(input("Digite o segundo numero\n"))

# Aritmétricos (3 % 2 = 1) / 4^2 = 4*4
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2
print(f"A soma de {num1} por {num2} deu como resposta: {sum}")
print(f"A subtração de {num1} por {num2} deu como resposta: {sub}")
print(f"O resto da divisão de {num1} por {num2} deu como resposta: {mod}")
print(f"O numero {num1} elevado ao número {num2} da como resposta o número: {exp}")

# Comparação 
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
diferent = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"O número {num1} é igual ao número {num2} ?: {equal}")
print(f"O núemro {num1} é maior ou igual ao número {num2} ?: {bigger_equal}")
print(f"O núemro {num1} é menor ou igual ao número {num2} ?: {smaller_equal}")

# Atribuição 

num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 /= 1 # num1 = num1 / 1
num1 *= 1 # num1 = num1 * 1
