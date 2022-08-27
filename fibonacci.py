def main(n):
    """
    This function prints the first n elements of the fibonacci sequence

    Args:
        n (int): Numero de elementos a imprimir
    """
    for i in range(1, n+1):
        print(sum(range(1, i+1)))


if __name__ == '__main__':
    main(50)
