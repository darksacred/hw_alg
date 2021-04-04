import numpy as np

def matrix(matrx1,matrx2):
    if range(len(matrx1[0])) != range(len(matrx2)):
        return ValueError(f'Произведение не определено')
    finish_matrx = [[0 for i in range(len(matrx1[0]))] for j in range(len(matrx2))]
    for i in range(len(matrx1)):
#        print(f'это i по м1:{i}')
        for j in range(len(matrx2[0])):
#            print(f'это j по м2:{j}')
            for k in range(len(matrx2)):
#                print(f'это k по м2:{k}')
                finish_matrx[i][j] += matrx1[i][k] * matrx2[k][j]
    return finish_matrx

a = np.array([[1,1],[2,2]])
b = np.array([[3,3],[4,4]])
print(f'NP:\n {np.dot(a,b)}')
print(f'Матрица: {matrix(a,b)}')
