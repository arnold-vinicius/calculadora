import calculadora
# Implementação da calculadora simples
while True:

    # apresentaçao
    print('\n\t\t\t --- Calculadora Simples --- \n')

    #menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

    # ler opções
    op = int(input('\n\tOpção: '))

    if op == 1:
        print('\nSoma\n')

        #entrada
        v1 = int(input('digite um numero: '))
        v2 = int(input('digite outro numero: '))

        #processamento
        total = calculadora.soma(v1,v2)

        #saida
        print(f'\n{v1} + {v2} = {total}\n')

    elif op == 2:
        print('\nSubtração\n')

        # entrada
        v1 = int(input('digite um numero: '))
        v2 = int(input('digite outro numero: '))

        #processamento
        total = calculadora.sub(v1,v2)

        #saida
        print(f'\n{v1} - {v2} = {total}\n')

    elif op == 3:
        print('\nMultiplicação\n')

        # entrada
        v1 = int(input('digite um numero: '))
        v2 = int(input('digite outro numero: '))

        #processamento
        total = calculadora.mult(v1,v2)

        #saida
        print(f'\n{v1} * {v2} = {total}\n')

    elif op == 4:
        print('\nDivisão\n')

        # entrada
        v1 = int(input('digite um numero: '))
        v2 = int(input('digite outro numero: '))

        #processamento
        total = calculadora.div(v1,v2)

        #saida
        print(f'\n{v1} / {v2} = {total}\n')

    elif op == 5:
        # Sair do sistema
        print('Obrigado pela preferência e um forte abraço')
        break
    else:
        #tratamento de exceção
        print(f'\nOpçao {op} incorreta!\n')