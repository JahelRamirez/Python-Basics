def main(n):
    """
    Esta funcion imprime solo los numeros primos
    de un rango del 1 al numero elegido.

    Args:
        n (int): Ultimo numero en el rango a imprimir
    """
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)


if __name__ == '__main__':
    main(50)
