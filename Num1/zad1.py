import numpy as np
import matplotlib.pyplot as plt

"""@Author: Jan Jochymczyk"""

x = 0.2 #zalozenie zadania

# Zalozenia zadania.
def f(x):
    return np.sin(x**2)

def df(x): #pochodna
    return 2*x*np.cos(x**2)

def przyb_a(f,x,h): #przyblizenie a)
    return (f(x+h)-f(x))/h

def przyb_b(f,x,h): #przyblizenie b)
    return (f(x+h)-f(x-h))/(2*h)

h_values = np.logspace(-20,10,100)  # zlogarytmowanie wartosci h

errors_float_a = [] #tu sa tablice dla bledow
errors_float_b = []
errors_double_a = []
errors_double_b = []

for h in h_values: #przeiterowanie przez kazde h i obliczenie bledow dla tego h
    result_float_a = przyb_a(f,np.float32(x),np.float32(h))
    result_float_b = przyb_b(f,np.float32(x),np.float32(h))
    result_double_a = przyb_a(f,np.float64(x),np.float64(h))
    result_double_b = przyb_b(f,np.float64(x),np.float64(h))
    error_float_a = np.abs(result_float_a -df(x))
    error_float_b = np.abs(result_float_b-df(x))
    error_double_a = np.abs(result_double_a-df(x))
    error_double_b = np.abs(result_double_b-df(x))
    errors_float_a.append(error_float_a)
    errors_float_b.append(error_float_b)
    errors_double_a.append(error_double_a)
    errors_double_b.append(error_double_b)

# wykres w skali logarytymicznej
plt.figure(figsize=(10,6))
plt.loglog(h_values, errors_float_a, label='Float (a)')
plt.loglog(h_values, errors_float_b, label='Float (b)')
plt.loglog(h_values, errors_double_a, label='Double (a)')
plt.loglog(h_values, errors_double_b, label='Double (b)')
plt.xlabel('h')
plt.ylabel('|Dhf(x)-f\'(x)|')
plt.legend()
plt.title('Blad przyblizenia pochodnej funkcji sin(x^2) przy x=0.2')
plt.grid(True)
plt.show()

