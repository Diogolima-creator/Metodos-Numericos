from sympy import sympify, symbols
import time
import os
def MethodBissec():
    while True:
        interval_positive, interval_negative = map(float, input('Coloque o intervalo (Ex: 0.3 5.2 | 1.5 0.2):').split())
        timer = int(input('0. Metodo Rapido ou 1. Metodo Explicativo'))
        
        print('intervalos:', interval_positive, interval_negative)

        if interval_positive > interval_negative:
            interval_positive, interval_negative = interval_negative, interval_positive

        print('1. | f(Kx) | < Epsilon')
        print('2. | Xk - X(k-1) | < Epsilon')

        stopalgorithm = int(input('Qual o criterio de parada?'))
        epsilon = float(input('Qual o valor do criterio de parada (Ex: 0.00000001 | 0.01)?'))
        equation = input('Insira a equação (Ex: x^3 - 9*x + 5): ')

        column_a = []
        column_b = []
        column_xk = []
        column_fxk = []


        if stopalgorithm == 1:
            valor = 100000000000000000
            equation_variable = 0
            x = symbols('x')
            f = sympify(equation)
            iteration = 0

            while True:
                print()
                print('ITERAÇÃO NUMERO:', iteration)
                column_a.append(interval_negative)
                column_b.append(interval_positive)
                print('Passo 1')
                time.sleep(timer)
                print('Para este método primeiro aplicaremos a formula da bissecção: x = (', interval_positive, ' + ',
                      interval_negative, ')/2')
                time.sleep(timer)
                equation_variable = (interval_positive + interval_negative) / 2
                column_xk.append(equation_variable)
                print('Resultado obtido da formula da bissecção:', equation_variable)
                time.sleep(timer)
                valor = f.subs(x, equation_variable)
                print('Agora aplicaremos na função o resultado obtido:', equation)
                time.sleep(timer)
                print('Resultado obtido da função para o valor de x igual a', equation_variable, 'foi:', valor)
                time.sleep(timer)
                column_fxk.append(valor)

                print()
                print('Passo 2')
                time.sleep(timer)
                print('Agora verificaremos se atingiu o criterio de parada:')
                time.sleep(timer)
                print(' | f(Kx) | < Epsilon:', valor, '<', epsilon)
                time.sleep(timer)

                if abs(valor) < epsilon:
                    print('Encontramos o numero proximo da raiz dentro do criterio de parada fornecido:', equation_variable)
                    print('Tabela')
                    print()
                    print('K     |      a      |      b      |      xk      |      f(xk)      |')
                    for i in range(iteration+1):
                        print(i, '     |      ', column_a[i], '      |      ', column_b[i], '      |      ', column_xk[i], '      |      ', column_fxk[i], '      |')
                    time.sleep(timer)
                    print()
                    print('===============================')
                    print('O que faremos agora?')
                    print('1. Desejo usar novamente o método')
                    print('2. Desejo escolher outro método')
                    print('3. Desejo encerrar o programa')
                    print('===============================')

                    response = int(input())
                    if response == 1:
                        os.system('cls')
                        break
                    elif response == 2:
                        os.system('cls')
                        return
                    elif response == 3:
                        exit()
                    else:
                        exit()

                print('Se não foi atingido, rodaremos mais uma vez o metodo')
                time.sleep(timer)
                print('Agora substituindo o valor da bissecção.')
                print('Se o valor obtido da função para o valor de X for '
                      'positivo substituiremos no'
                      ' intervalo positivo,e caso for negativo será no intervalo negativo.')

                time.sleep(timer)
                print('Intervalo negativo:', interval_negative)
                print('Intervalo positivo:', interval_positive)
                time.sleep(timer)

                if valor < 0:
                    interval_negative = equation_variable
                    print('O novo intervalo negativo é:', interval_negative)
                    time.sleep(timer)
                else:
                    interval_positive = equation_variable
                    print('O novo intervalo positivo é:', interval_positive)
                    time.sleep(timer)

                iteration = iteration + 1

        if stopalgorithm == 2:
            valor = 100000000000000000
            equation_variable = 0
            x = symbols('x')
            f = sympify(equation)
            iteration = 0
            x_array = [0]
            position = 1

            while True:
                print()
                print('ITERAÇÃO NUMERO:', iteration)
                column_a.append(interval_negative)
                column_b.append(interval_positive)
                print('Passo 1')
                time.sleep(timer)
                print('Para este método primeiro aplicaremos a formula da bissecção: x = (', interval_positive, ' + ',
                      interval_negative, ')/2')
                time.sleep(timer)
                equation_variable = (interval_positive + interval_negative) / 2
                x_array.append(equation_variable)
                column_xk.append(equation_variable)
                print('Resultado obtido da formula da bissecção:', equation_variable)
                time.sleep(timer)
                valor = f.subs(x, equation_variable)
                column_fxk.append(valor)
                print('Agora aplicaremos na função o resultado obtido:', equation)
                time.sleep(timer)
                print('Resultado obtido da função para o valor de x igual a', equation_variable, 'foi:', valor)
                time.sleep(timer)

                print()
                print('Passo 2')
                time.sleep(timer)
                print('Agora verificaremos se atingiu o criterio de parada:')
                time.sleep(timer)
                print(' | Xk - X(k-1) | < Epsilon', abs(x_array[position]-x_array[position-1]), '<', epsilon)
                time.sleep(timer)

                if abs(x_array[position]-x_array[position-1]) < epsilon:
                    print('Encontramos o numero proximo da raiz dentro do criterio de parada fornecido:',
                          equation_variable)
                    time.sleep(timer)
                    print('Tabela')
                    print()
                    print('K     |      a      |      b      |      xk      |      f(xk)      |')
                    for i in range(iteration + 1):
                        print(i, '     |      ', column_a[i], '      |      ', column_b[i], '      |      ',
                              column_xk[i], '      |      ', column_fxk[i], '      |')
                    print()
                    print('===============================')
                    print('O que faremos agora?')
                    print('1. Desejo usar novamente o método')
                    print('2. Desejo escolher outro método')
                    print('3. Desejo encerrar o programa')
                    print('===============================')

                    response = int(input())
                    if response == 1:
                        os.system('cls')
                        break
                    elif response == 2:
                        os.system('cls')
                        return
                    elif response == 3:
                        exit()
                    else:
                        exit()

                print('Se não foi atingido, rodaremos mais uma vez o metodo')
                time.sleep(timer)
                print('Agora substituindo o valor da bissecção.')
                print('Se o valor obtido da função para o valor de X for '
                      'positivo substituiremos no'
                      ' intervalo positivo,e caso for negativo será no intervalo negativo.')

                time.sleep(timer)
                print('Intervalo negativo:', interval_negative)
                print('Intervalo positivo:', interval_positive)
                time.sleep(timer)

                if valor < 0:
                    interval_negative = equation_variable
                    print('O novo intervalo negativo é:', interval_negative)
                    time.sleep(timer)
                else:
                    interval_positive = equation_variable
                    print('O novo intervalo positivo é:', interval_positive)
                    time.sleep(timer)

                position = position + 1
                iteration = iteration + 1

