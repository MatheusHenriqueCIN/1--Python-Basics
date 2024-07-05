name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrice = float(input("Digite o preço do jogo\n"))
planIncluded = bool(input("Está incluso em alguma assinatura?\n"))

print("### Dados do Jogo ###")
print("=====================")
# Alternativa 1
# print("Nome do Jogo:", name)
# print("Ano de lançamento do Jogo:", yearLaunch)
# print("Preço do Jogo", gamePrice)
# print("Está incluso assinatura no Jogo:", planIncluded)

# # Alternativa 2
# print("Nome do Jogo:", name, "\nAno de lançamento:" , yearLaunch,
# "\nPreço do Jogo:", gamePrice, "\nPlano está incluso?:", planIncluded)

# -------------Alternativa 3 (Melhor Alternativa)-----------------------
# print(f"Nome do Jogo: {name} \nAno de lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nAssinatura está incluso?: {planIncluded}")