soma = 0
listAprimorador = []
listEmissor = []
listTransmutador = []
listManipulador = []
listConjurador = []
listEspecialista = []


qtd_monitores = int(input())
while soma < qtd_monitores:
    monitor = input()
    mudanca = input()
    
    if monitor in listAprimorador:
        listAprimorador.remove(monitor)
    elif monitor in listConjurador:
        listConjurador.remove(monitor)
    elif monitor in listEmissor:
        listEmissor.remove(monitor)
    elif monitor in listEspecialista:
        listEspecialista.remove(monitor)
    elif monitor in listManipulador:
        listManipulador.remove(monitor)
    elif monitor in listTransmutador:
        listTransmutador.remove(monitor)
    
    if mudanca == "O volume da água foi alterado.":
        listAprimorador.append(monitor)
        soma += 1
    elif mudanca == "A cor da água foi alterada.":
        listEmissor.append(monitor)
        soma += 1
    elif mudanca == "O gosto da água foi alterado.":
        listTransmutador.append(monitor)
        soma+=1
    elif mudanca == "A folha se moveu.":
        listManipulador.append(monitor)
        soma += 1
    elif mudanca == "Impureza apareceram na água.":
        listConjurador.append(monitor)
        soma += 1
    else:
        listEspecialista.append(monitor)
        soma += 1

if len(listAprimorador) > 0:
    print(f"Temos um total de {len(listAprimorador)} aprimoradores entre os monitores! Eles são: ", end="")
    for i, monitor in enumerate(listAprimorador):
        if i > 0:
            print(", ", end="")
        print(monitor, end="")
if len(listEmissor) > 0:
    print(f"Temos um total de {len(listEmissor)} emissores entre os monitores! Eles são: ", end="")
    for i, monitor in enumerate(listEmissor):
        if i > 0:
            print(", ", end="")
        print(monitor, end="")
if len(listTransmutador) > 0:
    print(f"Temos um total de {len(listTransmutador)} transmutadores entre os monitores! Eles são: ", end="")
    for i, monitor in enumerate(listTransmutador):
        if i > 0:
            print(", ", end="")
        print(monitor, end="")
if len(listManipulador) > 0:
    print(f"Temos um total de {len(listManipulador)} manipuladores entre os monitores! Eles são: ", end="")
    for i, monitor in enumerate(listManipulador):
        if i > 0:
            print(", ", end="")
        print(monitor, end="")
if len(listConjurador) > 0:
    print(f"Temos um total de {len(listConjurador)} conjuradores entre os monitores! Eles são: ", end="")
    for i, monitor in enumerate(listConjurador):
        if i > 0:
            print(", ", end="")
        print(monitor, end="")
if len(listEspecialista) > 0:
    print(f"Temos um total de {len(listEspecialista)} especialistas entre os monitores! Eles são: ", end="")
    for i, monitor in enumerate(listEspecialista):
        if i > 0:
            print(", ", end="")
        print(monitor, end="")
