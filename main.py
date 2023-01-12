primos = [] #sera a lista de primos encontrados

x=int(input("Digite um numero inteiro: "))#numero ate onde devem ser verificados os primos

for numeros in range (2,x):#define "numeros" em um alcande de A-B

    for primo in primos: # instruções a serem executadas para cada elemento

        if (numeros % primo) == 0:#define numeros como uma variavel e testa se ele é divisivel por algum dos numeros anteriores, caso ele for não os adiciona a lista

            break

    else:#sera o responsavel por adicionar a lista

        primos.append(numeros)#caso validado ele adiciona na lista de primos os numeros

print(primos)#imprime os numeros primos adicionados na lista
