def print_matrix(matriz):
    for row in matriz:
        print(" ".join(str(n) for n in row))

matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

def soma_diagonal_principal(matriz):
    soma = 0 
    for i in range (len(matriz)):
        soma += matriz [i][i]
    return soma 