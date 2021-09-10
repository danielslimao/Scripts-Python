mul=1
soma=0
maior=0
for c in range(1,3):
    n=float(input('Digite o número {}: '.format(c)))
    mul=mul*n
    soma=soma+n
    if n>maior:
        maior=n
print('[1] SOMAR')
print('[2] MULTIPLICAR')
print('[3] MAIOR')
print('[4] NOVOS NÚMEROS')
print('[5] SAIR DO PROGRAMA')
opc = int(input('Digite uma das opções acima: '))
while opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5:
    opc = int(input('Digite uma opção válida: '))
while opc==1 or opc==2 or opc==3 or opc==4:
    if opc==1:
        print('A soma entre os valores é {}'.format(soma))
        nov= str(input('Ir novamente? ')).upper().strip()[0]
        if nov=='S':
            for c in range(1, 3):
                n = float(input('Digite o número {}: '.format(c)))
                mul = mul * n
                soma = soma + n
                if n > maior:
                    maior = n
            print('[1] SOMAR')
            print('[2] MULTIPLICAR')
            print('[3] MAIOR')
            print('[4] NOVOS NÚMEROS')
            print('[5] SAIR DO PROGRAMA')
            opc = int(input('Digite uma das opções acima: '))
        else:
            x = input('Programa encerrado!')
    elif opc==2:
        print('A multiplicação entre os valores é {}'.format(mul))
        nov = str(input('Ir novamente? ')).upper().strip()[0]
        if nov == 'S':
            for c in range(1, 3):
                n = float(input('Digite o número {}: '.format(c)))
                mul = mul * n
                soma = soma + n
                if n > maior:
                    maior = n
            print('[1] SOMAR')
            print('[2] MULTIPLICAR')
            print('[3] MAIOR')
            print('[4] NOVOS NÚMEROS')
            print('[5] SAIR DO PROGRAMA')
            opc = int(input('Digite uma das opções acima: '))
        else:
            x=input('Programa encerrado!')
    elif opc==3:
        print('O valor maior entre os escolhidos é {}'.format(maior))
        nov = str(input('Ir novamente? ')).upper().strip()[0]
        if nov == 'S':
            for c in range(1, 3):
                n = float(input('Digite o número {}: '.format(c)))
                mul = mul * n
                soma = soma + n
                if n > maior:
                    maior = n
            print('[1] SOMAR')
            print('[2] MULTIPLICAR')
            print('[3] MAIOR')
            print('[4] NOVOS NÚMEROS')
            print('[5] SAIR DO PROGRAMA')
            opc = int(input('Digite uma das opções acima: '))
        else:
            x = input('Programa encerrado!')
    elif opc==4:
        for c in range(1, 3):
            n = float(input('Digite o número {}: '.format(c)))
            mul = mul * n
            soma = soma + n
            if n > maior:
                maior = n
        print('[1] SOMAR')
        print('[2] MULTIPLICAR')
        print('[3] MAIOR')
        print('[4] NOVOS NÚMEROS')
        print('[5] SAIR DO PROGRAMA')
        opc = int(input('Digite uma das opções acima: '))

if opc==5:
    print('Programa encerrado!')









