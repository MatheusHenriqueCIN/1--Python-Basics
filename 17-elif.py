num1 = float(input("Digite o número 1\n"))
num2 = float(input("Digite o número 2\n"))
operation = input("Digite a operação a realizar (+ - / *)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-": # Elif é como se fosse: "se for outra coisa..."
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else: # Se não for nenhuma das variaveis acima mostre:
    print("Operação Inválida")
    result = 0
print(f"O resultado é: {result:.2f}") # Aqui irá mostrar o resultado de um dos if's acima
