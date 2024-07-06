# Wilhe você da um incremento pra tirar do infinito
gameName = input("Digite o nome do jogo\n")
qtdRating = 0   # Como é tipagem dinâmica tem que adicionar um valor no ínicio para não dar nenhum erro.
totalRating = 0
rating = 0
average = 0
while(rating != -1): # While = Enquanto | Enquanto não botar - 1 o laço continua
    rating = float(input("Informe a nota do jogo\n")) # Isso aqui ira se repetir até inserir -1
    if(rating != -1): # "Se o total rating for diferente de -1"
        totalRating += rating  # totalRating = totalRating + rating | isso aqui é soma de todas as notas, adicionando cada nota a mais inserida no input
        qtdRating += 1 # qtdRating = qtdRating + 1 | Aqui é a quantidade de vezes que aconteceu e ira ser o divisor para fornecer nossa média.
        average = totalRating / qtdRating # Aqui é o cálculo da média.
print(f"Média das avaliações do jogo {gameName} é {average:.2f}")