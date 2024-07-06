# Utilização dos If e Else

name = input("Digite o nome do Jogo\n")
yearLaunch = int(input("Digite o ano do Jogo\n"))
classification = float(input("Digite a nota de condição de Jogo\n"))


# Se o IF tiver Junto com "or" = se uma das duas estivar correta,passa.
if classification >= 8.0 or yearLaunch > 2015:
    print(f"O jogo {name} é bom. Recomendo o jogo")
else:
    print(f"O jogo {name} não é bom. Não recomendo o jogo")
    
# Se o IF tiver Junto com "and" = as duas tem que está correta para passar.
if classification >= 8.0 and yearLaunch > 2015:
    print(f"O jogo {name} é bom. Recomendo o jogo")
else:
    print(f"O jogo {name} não é bom. Não recomendo o jogo")
    