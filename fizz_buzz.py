def main():
    """
    This function prints the numbers from 1 to 100 in each line.
    If the number is a multiple of 3 it prints "Fizz".
    If the number is a multiple of 5 is prints "Buzz".
    If the number is a multiple of both it prints "fizzbuzz".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


if __name__ == '__main__':
    main()
