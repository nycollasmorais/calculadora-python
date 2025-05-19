while True:
    numero_1=input('Digite um número: ')
    numero_2=input('Digite outro número: ')
    operacao=input('Qual operação deseja realizar? (+-*/): ')
    float_1=0
    float_2=0
    numeros_validos = None

#conferindo se os numeros sao validos

    try:
        float_1=float(numero_1)
        float_2=float(numero_2)
        numeros_validos=True
    except:
        numeros_validos=None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

#conferindo o operador

    operadores='+-*/'
    if operacao not in operadores:
        print('Operador inválido!')
        continue

    if len(operacao)>1:
        print('Operador inválido!')
        continue


    if operacao=='+':
        print(f'O resultado é : {float_1+float_2}')
    elif operacao=='-':
        print(f'O resultado é : {float_1-float_2}')
    elif operacao=='*':
        print(f'O resultado é : {float_1*float_2}')
    else:
        if float_2==0:
            print('Não é possível dividir um número por zero!')
        else:
            print(f'O resultado é : {float_1/float_2}')
        

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

