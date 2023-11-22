import numpy as np
import matplotlib.pyplot as plt
import time

def shermanMorrison(n, b):
    print(f"\nWlasna implementacja dla N = {n}")
    A = [] #Zastosowanie triku na rozlozenie macierzy na [[1, ...] ...] + A - 1
    A.append([11] * n)
    A.append([7] * (n-1) + [0])

    start = time.time()

    z = [0] * n
    x = [0] * n
    z[n-1] = b[n-1] / A[0][n-1]
    x[n-1] = 1 / A[0][n-1]

    for i in range(n - 2, -1, -1):
        z[i] = (b[n-2] - A[1][i] * z[i+1]) / A[0][i]
        x[i] = (1 - A[1][i] * x[i+1]) / A[0][i]

    delta = sum(z) / (1+sum(x))

    y = []
    for i in range(len(z)):
        y.append(z[i] - x[i] * delta)

    end = time.time()
    print(y)
    return end-start

def checkNumpy(n, b):
    print(f"\nWynik z biblioteki numpy dla N = {n}")
    A = np.ones((n, n))
    A += np.diag([11] * n)
    A += np.diag([7] * (n - 1), 1)
    start = time.time()
    np.linalg.solve(A, b)
    end = time.time()
    print(np.linalg.solve(A, b))
    return end - start

def plot_execution_time():
    N = []
    num = []
    real = []
    for i in range(50, 15000, 200):
        n = i
        N.append(n)
        b = [5]*n

        num.append(checkNumpy(n, b))
        real.append(shermanMorrison(n, b))

    plt.grid(True)
    plt.title('Czas pracy programu.')
    plt.xlabel('n')
    plt.ylabel('mikrosekundy')
    plt.yscale('log')

    plt.plot(N, num)
    plt.plot(N, real)
    plt.legend(['Czas pracy biblioteki numpy', 'Czas pracy mojego algorytmu'])
    plt.show()
def main():
    checkNumpy(80, [5]*80)
    shermanMorrison(80, [5]*80)
    #plot_execution_time()

if __name__ == "__main__":
    main()
