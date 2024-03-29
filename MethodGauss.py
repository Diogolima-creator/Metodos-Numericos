from sympy import sympify, symbols
import time
import os
from fractions import Fraction

def printMatriz(matriz):
  for linha in matriz:
    linha_formatada = []
    for elemento in linha:
        if isinstance(elemento, int) or elemento.denominator == 1:
            linha_formatada.append(elemento.numerator if isinstance(elemento, Fraction) else elemento)
        else:
            linha_formatada.append(elemento)
    print(linha_formatada)

def resolver_sistema(arrays):
      n = len(arrays)
      respostas = [0] * n

      for i in range(n - 1, -1, -1):
          respostas[i] = arrays[i][-1]
          for j in range(i + 1, n):
              respostas[i] -= arrays[i][j] * respostas[j]
          respostas[i] /= arrays[i][i] if isinstance(arrays[i][i], Fraction) else float(arrays[i][i])

      return respostas
    # Resolver o sistema linear

def get_termo(indice):
      return f"x{indice}"

def Gauss ():
  while True:
    print()
    print('Metodo de Gauss consiste em transformar o sistema Ax=b em um sistema equivalente com matriz dos coeficientes triangular superior')
    print('Ax=b -> A~x=b~')
    print()
    print('Vamos ao teorema seja Ax=b um sistema linear')
    print('a) Trocarmos duas equacões')
    print('b) Multiplicarmos uma equação por uma constante nula')
    print('c) Adicionamos um multiplo de uma equação a outra equação')
    print() 
    print('Obteremos um sistema A~x=b~')
    print('Bem vamos ao metodo de eliminação de Gauss')
    print('Esse metodo engloba duas fases')
    print()
    print('i) Fase de Eliminação')
    print('ii) Fase de substituição')

    pivoL = 0
    print()
    timer = int(input('0. Metodo Rapido ou 1. Metodo Explicativo \n'))
    print()
    print('Procedimento: Fase de Eliminação')
    print('Primeiro precisamos montar a matriz')
    print('Para isso voce deve transformar as equacoes em linhas da matriz, exemplo:')
    print('Essa equação')
    print('2x - 4y + 3z = 2')
    print('Deve virar essa linha:')
    print('[2 -4 3 2]')
    print('Vamos lá')
    print()
    numL = int(input('Insira o numero de linhas da sua matriz \n'))
    matriz = []
 
    for i in range(0, numL):
            auxArray = []
            aux = input('Insira a linha ex: 3 5 2 4 7 \n')
            for j in aux.split():    
              auxArray.append(int(j))
            matriz.append(auxArray)
        
    print('A matriz digitada foi essa')
    printMatriz(matriz)

    while pivoL+1 != numL:
        print()
        print('Certo agora procurar pelo pivo, mas antes verificar se é necessario pivoteamento parcial')
        pivo = 0

        for i in range(pivoL, numL):
          if matriz[i][i] == 0:
              print('Pivoteamento parcial necessario')
              aux = 0
              for j in range(i, numL):
                 if(matriz[j][i] > aux):
                    aux = j
              print()
              print('Trocaremos as linhas:', [i+1],' ', [j+1])
              matriz[j], matriz[i] = matriz[i], matriz[j]
              pivo = matriz[i][i]
              printMatriz(matriz)
              break
          else:
            print('Não é necessario pivoteamento parcial.')
            pivo = matriz[i][i]
            break
        print()
        print('O Pivo sera:', pivo) 

        for i in range(pivoL+1, numL):
          pivoML = Fraction(matriz[i][pivoL], pivo)
          for j in range(0, len(matriz[0])):
            matriz[i][j] = matriz[i][j] - (pivoML * matriz[pivoL][j])
          
        printMatriz(matriz)
        time.sleep(1)
        pivoL = pivoL + 1
    print()
    print('Agora após transformarmos a matriz em uma matriz triangular superior, basta resolvermos o sistema')
    print()

    for i, linha in enumerate(matriz):
      termos = [f"{coeficiente}{get_termo(indice)}" for indice, coeficiente in enumerate(linha[:-1], 1)]
      igualdade = f" = {linha[-1]}"
      print(" + ".join(termos) + igualdade)
    sistema = resolver_sistema(matriz)
    print()
    for i, resposta in enumerate(sistema):
        print(f"{get_termo(i+1)} = {resposta}")

    print()
    print('===============================')
    print('O que faremos agora?')
    print('1. Desejo usar novamente o método')
    print('2. Desejo escolher outro método')
    print('3. Desejo encerrar o programa')
    print('===============================')

    response = int(input())
    if response == 1:
        print()
    elif response == 2:
        return
    elif response == 3:
        exit()
    else:
        exit()