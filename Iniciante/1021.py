'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''

valor = float(input())

print('NOTAS:')

print('{:.0f} nota(s) de R$ 100.00'.format(valor // 100))
valor = valor % 100

print('{:.0f} nota(s) de R$ 50.00'.format(valor // 50))
valor = valor % 50

print('{:.0f} nota(s) de R$ 20.00'.format(valor // 20))
valor = valor % 20

print('{:.0f} nota(s) de R$ 10.00'.format(valor // 10))
valor = valor % 10

print('{:.0f} nota(s) de R$ 5.00'.format(valor // 5))
valor = valor % 5

print('{:.0f} nota(s) de R$ 2.00'.format(valor // 2))
valor = valor % 2

print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(valor // 1.0))
valor = valor % 1

print('{:.0f} moeda(s) de R$ 0.50'.format(valor // 0.50))
valor = valor % 0.50

print('{:.0f} moeda(s) de R$ 0.25'.format(valor // 0.25))
valor = valor % 0.25

print('{:.0f} moeda(s) de R$ 0.10'.format(valor // 0.10))
valor = valor % 0.10

print('{:.0f} moeda(s) de R$ 0.05'.format(valor // 0.05))
valor = valor % 0.05

print('{:.0f} moeda(s) de R$ 0.01'.format(valor / 0.01))
