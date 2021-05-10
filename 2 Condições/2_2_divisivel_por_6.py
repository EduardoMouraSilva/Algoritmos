num = float(input('Digite um número: '))

if (num % 2 == 0):
    if (num % 3 == 0):
        print(f'{num} é divisível por 6.')
    else:
        print(f'{num} é divisível por 2, mas não por 3,', end=' ')
        print(f'então não é divisível por 6.')
elif (num % 3 == 0):
    if (num % 2 == 0):
        print(f'{num} é um número divisível por 6.')
    else:
        print(f'{num} é divisível por 3, mas não por 2,', end=' ')
        print('então não é divisível por 6.')
else:
    print(f'{num} não é divisível por 6.')
