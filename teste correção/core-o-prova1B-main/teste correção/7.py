def A():
    lista = [x for x in range (5)]
    print(lista)


def B():
    lista =list(range(5))
    print(lista)

def C():
    lista = []
    i = 0
    while i < 5:
        lista.append(i)
        i += 1 
    print(lista)

lista_A = A()
lista_B = B()
lista_C = C()

#saidas:
#[0, 1, 2, 3, 4]
#[0, 1, 2, 3, 4]
#[0, 1, 2, 3, 4]
#resposta correta: d)
#resposta que havia marcado: A)
#falta de conecimento que que a lista já estava sendo gerada.