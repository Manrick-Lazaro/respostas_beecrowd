'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''

# quando declaramos mais de uma variavel a um input com o uso de uma função split
# para cada elemento separado será instanciado em uma variavel.

# mas em compesação se vc fizer um split em mais objetos do que a quantidade de 
# variaveis declaradas ocorrerá um erro.

# dito isto, vamos adicionar uma função map() no input. A função map recebe dois parametros
# uma função e uma lista. para cada elemento da lista será aplicada a função passada no parametro.

# por fim, é possivel que na mesma linha possamos criar mais de uma variavel aplicando o casting 
# de imediato.

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print('{:.4f}'.format(distancia))
