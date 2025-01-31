x = 0
list = []

while x == 0:
    y = str(input())
    if y == "Novo vilão - Muito Perigoso":
        vilao = str(input())
        list.insert(0, vilao)
    elif y == "Novo vilão - Meio perigoso":
        vilao = str(input())
        list.append(vilao)
    elif y == "O que ele está fazendo aqui?":
        vilao = str(input())
        list.remove(vilao)
    elif y == "Vilão mais perigoso do que pensávamos":
        index1 = int(input())
        index2 = int(input())
        list[index1], list[index2] = list[index2], list[index1]
    elif y == "Que estranho, esses dois vilões… troque-os de lugar":
        vilao = str(input())
        vilao2 = str(input())
        index1 = list.index(vilao)
        index2 = list.index(vilao2)
        list[index1], list[index2] = list[index2], list[index1]
    elif y == "Essa posição não está de acordo, ele nem odeia carecas":
        vilao = str(input())
        list.remove(vilao)
        list.append(vilao)
    elif y == "Como a lista está ficando?":
        print(*list, sep=', ')
    elif y == "Já temos nossa lista de vilões":
        x += 1
print(f"O resultado final ficou assim:", *list, sep=", ")
