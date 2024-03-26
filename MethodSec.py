from sympy import sympify, symbols
import time
import os

def MethodSecante():
    while True:
        print()
        print('==========')
        print('')

        x0, x1 = map(float, input('Insira o valor de x0 e o x1 (Ex: 0.3 5.2 | 1.5 0.2):').split())
        if x0 > x1:
            x0, x1 = x1, x0

        timer = int(input('0. Metodo Rapido ou 1. Metodo Explicativo'))
        equation = input('Insira a equação (Ex: x^3 - 9*x + 5): ')
        epsilon = float(input('Qual o valor do criterio de parada (Ex: 0.00000001 | 0.01)?'))

        equation_variable = [x0, x1]
        x = symbols('x')
        f = sympify(equation)
        iteration = 2

        column_fxk = []
        print()
        print('Primeiro calcularemos o valor de f(x0) e f(x1)')
        valor_x0 = f.subs(x, equation_variable[0])
        valor_x1 = f.subs(x, equation_variable[1])
        print('Valor obtido para f(x0):', valor_x0)
        print('Valor obtido para f(x1):', valor_x1)
        column_fxk.append(valor_x0)
        column_fxk.append(valor_x1)
        print('Agora começaremos o metodo, porém apartir da segunda interação')

        while True:
            print()
            print('Iteração: ', iteration)
            print('Metodo Da Secante')
            print('A formula do metodo é: Xk+1 = Xk - f(Xk)*(Xk-X(k-1))/f(Xk)-f(X(k-1))')

            time.sleep(timer)
            div_num = column_fxk[iteration-1]*(equation_variable[iteration-1] - equation_variable[iteration-2])
            div_den = column_fxk[iteration-1]-column_fxk[iteration-2]

            equation_variable.append(equation_variable[iteration-1] - (div_num/div_den))

            print('X',iteration,'é igual:', equation_variable[iteration])
            time.sleep(timer)
            print('Aplicado a formula temos agora X',iteration,'e vamos calcular seu f(x',iteration,')')
            time.sleep(timer)
            valor = f.subs(x, equation_variable[iteration])
            print('f(x',iteration,') é igual:', valor)
            time.sleep(timer)
            column_fxk.append(valor)
            print('Vamos conferir o criterio de parada:')
            print(abs(valor),'<',epsilon)
            if abs(valor) > epsilon:
                print('Vimos que não foi atingido')
                time.sleep(timer)
                print('Então precisaremos de mais uma iteração do metodo, vamos para a iteração', iteration+1)
                time.sleep(timer)
            else:
                print()
                print('Encontramos o numero proximo da raiz dentro do criterio de parada fornecido:',
                      equation_variable[iteration])
                time.sleep(timer)
                print()
                print('Tabela')
                print('K     |      xk      |      f(xk)      |')
                for i in range(iteration+1):
                    print(i, '   |      ', equation_variable[i], '      |      ', column_fxk[i], '      |')

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
            iteration = iteration + 1