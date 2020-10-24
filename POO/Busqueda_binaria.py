import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    if comienzo > final:
        return False


    medio = (final+comienzo) // 2

    if lista[medio] == objetivo:
        return True

    elif lista[medio] < objetivo:

        return busqueda_binaria(lista, medio + 1, final, objetivo)

    else :
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__=='__main__':
    tamano_de_lista = int(input('De que tamaño será la lista? '))
    objetivo = int(input('El número a buscar? '))

    lista=sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    print(lista)
    encontrar = busqueda_binaria(lista, 0, len(lista),objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrar else "no esta"} en la lista')
