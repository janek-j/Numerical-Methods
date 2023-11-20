from functools import reduce
import numpy as np
import time
import matplotlib.pyplot as plt

def fill_matrix(n):
    matrix = []
    matrix.append([0] + [0.2] * (n - 1))
    matrix.append([1.2] * n)
    matrix.append([0.1 / i for i in range(1, n)] + [0])
    matrix.append([0.15 / i**2 for i in range(1, n-1)] + [0] + [0])
    return matrix

def lu_decomposition(matrix, n):
    for i in range(1, n-2):
        matrix[0][i] = matrix[0][i] / matrix[1][i - 1]
        matrix[1][i] = matrix[1][i] - matrix[0][i] * matrix[2][i - 1]
        matrix[2][i] = matrix[2][i] - matrix[0][i] * matrix[3][i - 1]

    matrix[0][n-2] = matrix[0][n-2] / matrix[1][n-3]
    matrix[1][n-2] = matrix[1][n-2] - matrix[0][n-2] * matrix[2][n-3]
    matrix[2][n-2] = matrix[2][n-2] - matrix[0][n-2] * matrix[3][n-3]

    matrix[0][n-1] = matrix[0][n-1] / matrix[1][n-2]
    matrix[1][n-1] = matrix[1][n-1] - matrix[0][n-1] * matrix[2][n-2]

def forward_substitution(matrix, x):
    for i in range(1, len(matrix[0])):
        x[i] = x[i] - matrix[0][i] * x[i - 1]

def backward_substitution(matrix, x):
    x[-1] = x[-1] / matrix[1][-1]
    x[-2] = (x[-2] - matrix[2][-2] * x[-1]) / matrix[1][-2]

    for i in range(len(matrix[0]) - 3, -1, -1):
        x[i] = (x[i] - matrix[3][i] * x[i + 2] - matrix[2][i] * x[i + 1]) / matrix[1][i]

def calculate_determinant(matrix):
    return reduce(lambda a, b: a * b, matrix[1])

def check_numpy(n):
    A = np.diag([0.2] * (n - 1), -1)
    A += np.diag([1.2] * n)
    A += np.diag([0.1 / i for i in range(1, n)], 1)
    A += np.diag([0.15 / i**2 for i in range(1, n-1)], 2)
    x = list(range(1, n + 1))

    start = time.time()
    np_solution = np.linalg.solve(A, x)

    print("Czas numpy to: {:.20f}".format(time.time()-start))
    print(f"Rozwiązanie numpy: {np_solution}")

def main():
    n = 124

    matrix = fill_matrix(n)
    x = list(range(1, n + 1))

    start = time.time()

    lu_decomposition(matrix, n)
    forward_substitution(matrix, x)
    backward_substitution(matrix, x)

    determinant = calculate_determinant(matrix)
    end = time.time() - start

    print("Szukane rozwiązanie to:", x)
    print()
    print("Wyznacznik macierzy A =", determinant)

    # Testy
    check_numpy(n)

    #Rysowanie wykresu.
    n_values = list(range(50, 1001, 10))  # Zakres wartości n
    times = []

    for n in n_values:
        matrix = fill_matrix(n)
        x = list(range(1, n + 1))
        start = time.time()
        lu_decomposition(matrix, n)
        forward_substitution(matrix, x)
        backward_substitution(matrix, x)
        determinant = calculate_determinant(matrix)
        end = time.time() - start
        times.append(end)
        print(f"n = {n}, Czas wykonania: {end:.6f} sekundy")

    # Rysowanie wykresu
    plt.plot(n_values, times, marker='o')
    plt.title('Czas wykonania programu w zależności od n')
    plt.xlabel('n')
    plt.ylabel('Czas [s]')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
