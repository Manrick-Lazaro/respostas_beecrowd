'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

valor = int(input())

print('{}'.format(valor))

print('{} nota(s) de R$ 100,00'.format(valor // 100))
valor = valor % 100

print('{} nota(s) de R$ 50,00'.format(valor // 50))
valor = valor % 50

print('{} nota(s) de R$ 20,00'.format(valor // 20))
valor = valor % 20

print('{} nota(s) de R$ 10,00'.format(valor // 10))
valor = valor % 10

print('{} nota(s) de R$ 5,00'.format(valor // 5))
valor = valor % 5

print('{} nota(s) de R$ 2,00'.format(valor // 2))
valor = valor % 2

print('{} nota(s) de R$ 1,00'.format(valor // 1))
