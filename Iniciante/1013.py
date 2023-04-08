'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

val = input().split(' ')

maior = int(val[0])

if int(val[1]) > int(val[0]) and int(val[1]) > int(val[2]):
    maior = int(val[1])
elif int(val[2]) > int(val[0]) and int(val[2]) > int(val[1]):
    maior = int(val[2])

print('{} eh o maior'.format(maior))
