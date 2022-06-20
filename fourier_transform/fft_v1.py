# Transformada rápida de Fourier
# Autores: Grupo 1 - Dinámica de suelos

## Librerias
import numpy as np

## Transformada rápida de Fourier

def FFT(x):
    """
    x: vector unidimensional del registro (aceleración, velocidad o desplazamiento)
    La entrada debe ser potencia de 2, basado en el 1D Cooley-Tukey FFT
    """
    N = len(x)

    if N == 1:
        return x
    else:
        X_par = FFT(x[::2])
        X_impar = FFT(x[1::2])
        factor = np.exp(-2j* np.pi * np.arange(N)/N)

        X = np.concatenate(
            [X_par + factor[:int(N/2)]*X_impar,
             X_par + factor[int(N/2):]*X_impar]
        )
        return X
def DFT(x):
    """
    x: vector unidimensional del registro (aceleración, velocidad o desplazamiento)
    Función discreta de Fourier, para una señal 1D
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)

    return X


