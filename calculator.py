while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite um operador: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except Exception:
        numeros_validos = None

    if numeros_validos is None:
        print('numeros digitados são invalidos')

    operadores_premitidos = '+-/*'

    if operador not in operadores_premitidos:
        print('operador digitado está invalido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    print('seu numero esta sendo calculado, confira o resultado abaixo')

    if operador == '+':
        print(num_1_float + num_2_float)

    elif operador == '-':
        print(num_1_float - num_2_float)

    elif operador == '*':
        print(num_1_float * num_2_float)

    elif operador == '/':
        print(num_1_float / num_2_float)

    sair = input('voce quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
