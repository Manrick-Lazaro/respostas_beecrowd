'''

Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

'''
import math

valores = input().split(' ')

areaTriangulo = (float(valores[0]) * float(valores[2])) / 2
areaCirculo = (pow(float(valores[2]), 2)) * 3.14159
areaTrapezio = ((float(valores[0]) + float(valores[1])) * float(valores[2])) / 2
areaQuadrado = pow(float(valores[1]), 2)
areaRetangulo = float(valores[0]) * float(valores[1])

print('TRIANGULO: {:.3f}'.format(areaTriangulo))
print('CIRCULO: {:.3f}'.format(areaCirculo))
print('TRAPEZIO: {:.3f}'.format(areaTrapezio))
print('QUADRADO: {:.3f}'.format(areaQuadrado))
print('RETANGULO: {:.3f}'.format(areaRetangulo))
