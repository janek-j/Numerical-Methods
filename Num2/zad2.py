#Zadanie 2

import random

"""@Author: Jan Jochymczyk"""

import numpy as np

A1 = np.array([
    [2.554219275, 0.871733993, 0.052575899, 0.240740262, 0.316022841],
    [0.871733993, 0.553460938, -0.070921727, 0.255463951, 0.707334556],
    [0.052575899, -0.070921727, 3.409888776, 0.293510439, 0.847758171],
    [0.240740262, 0.255463951, 0.293510439, 1.108336850, -0.206925123],
    [0.316022841, 0.707334556, 0.847758171, -0.206925123, 2.374094162]
])

A2 = np.array([
    [2.645152285, 0.544589368, 0.009976745, 0.327869824, 0.424193304],
    [0.544589368, 1.730410927, 0.082334875, -0.057997220, 0.318175706],
    [0.009976745, 0.082334875, 3.429845092, 0.252693077, 0.797083832],
    [0.327869824, -0.057997220, 0.252693077, 1.191822050, -0.103279098],
    [0.424193304, 0.318175706, 0.797083832, -0.103279098, 2.502769647]
])

b = np.array([-0.642912346, -1.408195475, 4.595622394, -5.073473196, 2.178020609])  #definicja wektora

delta_b = random.randint(1, 10) * 1e-6

y1 = np.linalg.solve(A1, b) #rozwiazanie dla A1
y2 = np.linalg.solve(A2, b) #rozwiazanie dla A2

y1_zaburzone = np.linalg.solve(A1, b + delta_b) #rozwiazanie dla A1 z zaburzonym wektorem 
y2_zaburzone = np.linalg.solve(A2, b + delta_b) #rozwiazanie dla A2 z zaburzonym wektorem

print("Rozwiązanie A1y1 = b:")
print(y1)
print("\nRozwiązanie A2y2 = b:")
print(y2)

print("\nRozwiązanie A1y1 = b + delta_b:")
print(y1_zaburzone)
print("\nRozwiązanie A2y2 = b + delta_b") 
print(y2_zaburzone)

#Tu obliczam wspolczynniki uwarunkowania macierzy 
k1 = np.linalg.cond(A1) # Oblicza wspolczynniki uwarunkowania macierzy
print(f"\nWspolczynnik uwarunkowania macierzy A1 wynosi {k1}")
k2 = np.linalg.cond(A2)
print(f"Wspolczynnik uwarunkowania macierzy A2 wynosi {k2}")