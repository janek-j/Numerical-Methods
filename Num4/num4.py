import numpy as np
import matplotlib.pyplot as plt
import time

def shermanMorrison(n, b):
    print(f"\nWlasna implementacja dla N = {n}")
    A = []
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

    end = time.time() - start
    print(y)
    return end

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
    n_values = list(range(10, 800, 150))
    custom_implementation_times = []
    numpy_implementation_times = []

    for n in n_values:
        b = [5] * n
        custom_time = shermanMorrison(n, b)
        numpy_time = checkNumpy(n, b)
        custom_implementation_times.append(custom_time)
        numpy_implementation_times.append(numpy_time)

    plt.plot(n_values, custom_implementation_times, label='Wlasna implementacja')
    plt.plot(n_values, numpy_implementation_times, label='NumPy')
    plt.xlabel('N')
    plt.ylabel('Czas wykonania (s)')
    plt.title('Wykres czasu wykonania w zależności od N')
    plt.legend()
    plt.show()

def main():
    n = 80
    b = [5] * n
    shermanMorrison(n, b)
    checkNumpy(n, b)
    plot_execution_time()

if __name__ == "__main__":
    main()
