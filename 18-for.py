# Utilização básica do for

gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando valores de uma lista.
for game in gamesList:
    print(game)
    
# 2 - Quando a condição for atendida, o loop será encerrado
for game in gamesList:
    if game == "Red Dead 2":
        break
    print(game)  # Aqui ele só ira fornecer apenas os dois primeiros games da lista, já que no Red Dead ele para.
    
# 3 - Quando a condição for atendida, o loop vai para a próxima lista;
for game in gamesList:
    if game == "Red Dead 2":
        continue
    print(game)    # Aqui ele pura tal interação, como o exemplo foi o Red Dead ele já vai direto para uncharted.
    
# 4 - Avaliação de um jogo
gameName = input("Digite o nome do jogo\n") # Aqui ira escolher o nome do Jogo
gameRating = int(input("Digite quantas avaliações deseja fazer no projeto\n")) # Aqui você ira dizer quantas avaliações ira fazer

sum = 0 # Pra não dar nenhum problema se começa em 0 para somar certinho
for i in range(gameRating):  # Aqui delimita quantas fezes irá aparece a mensagem abaixo
    note = float(input("Digite a nota para o jogo\n"))
    sum += note # Isso aqui é a mesma coisa de sum = sum + note / que no caso é a soma das notas para fazer a média
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating}") # Aqui ira fazer a divisão, com a soma das notas sobre o número total selecionado de notas.
    