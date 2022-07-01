# Funciones de transferencia - PC05
# Autor: César Manuel Sánchez Oré

# Librerias
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Datos de entrada
h_1, h_2 = 4.5/100, 2.5/100 
Vs_1, Vs_2 = 145, 700 
# Vs_1, Vs_2 = 900, 700 
rho_1, rho_2 = 1.65, 1.8
H = 25
freq_range = 100
    
# Creación de DataFrame
data = pd.DataFrame(
    {
        "Freq" : np.arange(0, freq_range, 0.5)
    }
)

# Cálculos
G_1 = rho_1 * (Vs_1 ** 2)
G_2 = rho_2 * (Vs_2 ** 2)
G_1_complex = G_1 * (1 + 2 * h_1 * 1j) 
G_2_complex = G_2 * (1 + 2 * h_2 * 1j)

p_1 = data["Freq"] /(Vs_1 * ((1 + 2 * h_1 * 1j) ** 0.5))
p_2 = data["Freq"] /(Vs_2 * ((1 + 2 * h_2 * 1j) ** 0.5))
alpha = (G_1_complex * rho_1 / (G_2_complex * rho_2)) ** 0.5 

data["2E1/E2+F2"] = np.abs(1 / np.cos(p_1 * H))
data["2E1/2E2"] = np.abs(1 / (1j * alpha * np.sin(p_1 * H) + np.cos(p_1 * H))) 

# Ploteo de las gráficas

# Función de transferencia 2E1/E2+F2

fig_1 = go.Figure()

# Función a plotear
fig_1.add_trace(go.Scatter(
    x = data["Freq"],
    y = data["2E1/E2+F2"],
    mode = "lines",
    name = "Respuesta 1",
    marker = dict(color = "LightSkyBlue")
))

# Titulo general y de los ejes
fig_1.update_layout(xaxis_title = "Frecuencia (Hz)",
                       yaxis_title = "2E1/(E2 + F2)",
                       title = "Función de transferencia - Caso 1",
                      font = dict(size = 18)
                      ) 

# Formato de la gráfica
fig_1.update_xaxes(ticks = "outside",
                 tickwidth = 1,
                 tickcolor = "black",
                 ticklen = 5,
                 showline=True,
                 linewidth=1,
                 linecolor='black',
                 mirror=True)
fig_1.update_yaxes(ticks = "outside",
                 tickwidth = 1,
                 tickcolor = "black",
                 ticklen = 5,
                 showline=True,
                 linewidth=1,
                 linecolor='black',
                 mirror=True)
fig_1.update_layout(template = "plotly_white")

fig_1.show()

# Función de transferencia 2E1/2E2
fig_2 = go.Figure()

# Función a plotear
fig_2.add_trace(go.Scatter(
    x = data["Freq"],
    y = data["2E1/2E2"],
    mode = "lines",
    name = "Respuesta 1",
    marker = dict(color = "lightsalmon")
))

# Titulo general y de los ejes
fig_2.update_layout(xaxis_title = "Frecuencia (Hz)",
                       yaxis_title = "2E1/2E2",
                       title = "Función de transferencia - Caso 1",
                      font = dict(size = 18)
                      ) 

# Formato de la gráfica
fig_2.update_xaxes(ticks = "outside",
                 tickwidth = 1,
                 tickcolor = "black",
                 ticklen = 5,
                 showline=True,
                 linewidth=1,
                 linecolor='black',
                 mirror=True)
fig_2.update_yaxes(ticks = "outside",
                 tickwidth = 1,
                 tickcolor = "black",
                 ticklen = 5,
                 showline=True,
                 linewidth=1,
                 linecolor='black',
                 mirror=True)
fig_2.update_layout(template = "plotly_white")

fig_2.show()
