from sympy import sympify, symbols
import time
import os

def MethodNewtonR():
    while True:
        print()
        print('Antes de passar o Intervalo e a função que será trabalhada, certifique-se que:')
        print('As condições de convergencia sejam respeitados.')
        print('São essas:')
        print('i) f(x), f`(), f``(), são continuas no intervalo')
        print('ii) f`() != 0')
        print('iii) Xzero esta suficiente proximo da raiz')
        print('==========')
        print('')

        timer = int(input('0. Metodo Rapido ou 1. Metodo Explicativo'))
        equation = input('Insira a equação (Ex: x^3 - 9*x + 5): ')
        epsilon = float(input('Qual o valor do criterio de parada (Ex: 0.00000001 | 0.01)?'))
        x_zero = float(input('Qual o valor inicial de x0? (um chute dentro do intervalo dado)'))
        equation_variable = x_zero
        x = symbols('x')
        f = sympify(equation)
        derivada_f = f.diff(x)
        g = sympify(derivada_f)
        iteration = 0

        column_xk = []
        column_fxk = []
        column_fxk_derivada = []

        while True:
            print()
            print('Iteração: ', iteration)
            print('Calcularemos o valor de f(x) para x', iteration)
            time.sleep(timer)
            column_xk.append(equation_variable)
            valor = f.subs(x, equation_variable)
            column_fxk.append(valor)
            print('Resultado obtido:', valor)
            time.sleep(timer)
            print()
            print('Agora avaliaremos se atingimos o valor do criterio de parada')
            time.sleep(timer)
            print('|', valor,'|', '>', epsilon)
            time.sleep(timer)
            if abs(valor) > epsilon:
                print('Vimos que não foi atingido, agora calcularemos o x', iteration+1)
                time.sleep(timer)
                valor_derivada = g.subs(x, equation_variable)
                column_fxk_derivada.append(valor_derivada)
                print()
                print('Pegamos a sua derivada:', derivada_f)
                time.sleep(timer)
                print('E calcularemos sua f`(x)', iteration)
                time.sleep(timer)
                print('Agora aplicaremos a formula do método de Newton-Raphson:', equation_variable,'-', '(F(x):',valor,'/F`(x):',valor_derivada,')')
                time.sleep(timer)
                equation_variable = equation_variable - (valor/valor_derivada)
                print('Resultado obtido para o novo x', iteration+1, 'foi:', equation_variable)
            else:
                column_fxk_derivada.append('')
                print('Encontramos o numero proximo da raiz dentro do criterio de parada fornecido:',
                      equation_variable)
                print('Tabela')
                print('K     |      xk      |      f(xk)      |      f`(xk)      |')
                for i in range(iteration+1):
                    print(i, '   |      ', column_xk[i], '      |      ', column_fxk[i], '      |      ', column_fxk_derivada[i], '      |')

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