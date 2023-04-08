'''

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.


Exemplos de Entrada	
12 1 5.30
16 2 5.10

Exemplos de Saída
VALOR A PAGAR: R$ 15.50

'''

peca_01 = input().split(' ')
peca_02 = input().split(' ')

valor_peca_01 = int(peca_01[1]) * float(peca_01[2])
valor_peca_02 = int(peca_02[1]) * float(peca_02[2])

total = valor_peca_01 + valor_peca_02

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
