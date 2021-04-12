import numpy as np
from numpy.linalg import norm
np.set_printoptions(precision=2, suppress=True)

A = np.array([[1, 2, 0],
              [0, 0, 5],
              [3, -4, 2],
              [1, 6, 5],
              [0, 1, 0]])
print(f'Матрица A:\n{A}')

U, s, W = np.linalg.svd(A)

# Транспонируем матрицу W
V = W.T

print(f'Матрица U:\n{U}')
print(f'Матрица s:\n{s}')
print(f'Матрица V:\n{V}')

# s - список диагональных элементов, его нужно привести к виду диагональной матрицы для наглядности
D = np.zeros_like(A, dtype=float)
D[np.diag_indices(min(A.shape))] = s

print(f'Матрица со списком диагональных элементов D:\n{D}')

print(f'Матрица U:\n{U}')
# Убедимся, что она действительно ортогональна
print(f'Ортогональнасть U:\n{np.dot(U.T, U)}')
print(f'Матрица V:\n{V}')
# Убедимся, что она действительно ортогональна
print(f'Ортогональнасть V:\n{np.dot(V.T, V)}')
# Проведем проверку
print(f'Проверка (U*D)*Vt:\n{np.dot(np.dot(U, D), V.T)}')

print(f'Норма вектора D: {norm(D, ord=2)}')
print(f'Норма Фробениуса D: {np.sqrt(np.sum(D**2))}')
print(f'Норма вектора A: {norm(A, ord=2)}')
print(f'Норма Фробениуса A: {np.sqrt(np.sum(A**2))}')


