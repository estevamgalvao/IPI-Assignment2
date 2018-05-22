numFatias, numPremiado = input().split()
numFatias, numPremiado = [int(numFatias), int(numPremiado)]

listaNomes = []
listaFatias = []

for i in range(numFatias):
    Nome, Fatia = input().split()
    Fatia = int(Fatia)

    listaFatias.append(Fatia)
    listaNomes.append(Nome)

# print(listaFatias)
# print(listaNomes)

if listaFatias[0] == numPremiado:
    print(listaNomes[0])
else:
    for j in range(len(listaFatias)):
        # print(listaFatias[j])
        # print(numPremiado)
        if listaFatias[j] == numPremiado:
            print(listaNomes[j])
        else:
            numPremiado -= 1