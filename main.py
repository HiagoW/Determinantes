def mostrar(matriz, m, n):
    for c in range(n):
        print()
        for d in range(m):
            print(matriz[d][c], end="  ")


def sarrus(matriz):
    diag1 = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (
                matriz[0][2] * matriz[1][0] * matriz[2][1])
    diag2 = (matriz[0][2] * matriz[1][1] * matriz[2][0]) + (matriz[0][1] * matriz[1][0] * matriz[2][2]) + (
                matriz[0][0] * matriz[1][2] * matriz[2][1])
    det = diag1 - diag2
    return det


def laplace(matriz):
    soma = 0
    for j2 in range(4):
        c = 0;
        d = 0;
        cofator = [['-' for jco in range(3)] for ico in range(3)]
        mult = (-1)**(1 + (j2+1))
        for j in range(4):
            for i in range(4):
                if (i != 0) & (j != j2):
                    cofator[c][d] = matriz[j][i]
                    if d < 2:
                        d += 1
                    else:
                        c += 1
                        d = 0
        det=sarrus(cofator)
        soma += matriz[j2][0]*(det * mult)
    print(soma)


escolha=int(input('Escolha uma opção:\n'
                  '1-2x2\n'
                  '2-3x3\n'
                  '3-4x4\n'
                  '\n'))
if(escolha==1):
    m=2
    n=2
elif(escolha==2):
    m=3
    n=3
elif(escolha==3):
    m=4
    n=4

matriz = [['-' for j in range(n)] for i in range(m)]
for j in range(n):
    for i in range(m):
        print("\n\n")
        matriz[i][j] = int(input('Digite o elemento {}x{} da matriz: '.format(i + 1, j + 1)))
        mostrar(matriz, m, n)

print()

if escolha==1:
    det=(matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0])
    print('O determinante é: {}'.format(det))
elif escolha==2:
    print('O determinante é: {}'.format(sarrus(matriz)))
elif escolha==3:
    laplace(matriz)
