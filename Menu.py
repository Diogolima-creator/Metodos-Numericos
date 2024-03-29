import MethodBissec
import MethodNewtonR
import MethodSec
import MethodGauss

ListMethods = ['1. Método da Bisseção', '2. Método de Newton-Raphson', '3. Método da Secante', '4. Método de Eliminação de Gauss',
               '5. Método de Eliminação de Gauss com Pivoteamento Parcial', '5. Fatoração LU', '6. Fatoração LU com Pivoteamento Parcial']

def menu():
    print('############')
    for i in ListMethods:
            print(i)
    choicemethod = int(input('Escolhe o metodo:'))

    if choicemethod == 1:
        MethodBissec.MethodBissec()
    elif choicemethod == 2:
        MethodNewtonR.MethodNewtonR()
    elif choicemethod == 3:
        MethodSec.MethodSecante()
    elif choicemethod == 4:
         MethodGauss.Gauss()
    print('############')