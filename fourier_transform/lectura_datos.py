## Librerias
import matplotlib.pyplot as plt
import pandas as pd
from fft_v1 import *

plt.style.use('seaborn-poster')

## Lectura de datos
data = pd.read_csv("LIMA 74 N-S.txt",sep = "\t", header = None, names = ["t", "a"])
print(data)


data_corrected= np.concatenate((data["a"].to_numpy(), np.zeros(8192 - len(data["a"].to_numpy()))))
X = FFT(data_corrected)

## Cálculo de la frecuencia

N = len(X)
n = np.arange(N)
T = len(data["a"].to_numpy()) * 0.02
freq = n/T

data_2 = pd.read_csv("frequencias.txt", header = None, names = ["freq"])

freq = data_2["freq"].to_numpy()

X = X * 100 / N

#plt.stem(freq, abs(X),'b', markerfmt=" ", basefmt="-b")
plt.show()

# Salida de datos

data_salida = pd.DataFrame({
    "Frecuencia" : freq,
    "Amplitud": abs(X)
})

data_salida.to_excel("Resultados.xlsx")
