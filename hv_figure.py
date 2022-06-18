import pandas as pd
import plotly.graph_objects as go

# Entrada de datos
data = pd.read_csv("Puente_PiedraM.hv", 
                   skiprows = 9, 
                   names = ["Frequency", "Average", "Min", "Max"],
                   sep = "\s+")

# Ploteo de la imagen
x = data["Frequency"].to_list()
x_rev = x[::-1]

y = data["Average"].to_list()
y_upper = data["Max"].to_list()

y_lower = data["Min"].to_list()
y_lower = y_lower[::-1]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x+x_rev,
    y=y_upper+y_lower,
    fill='toself',
    fillcolor='rgba(0,100,80,0.2)',
    line_color='rgba(255,255,255,0)',
    showlegend=False,
    name='Fair',
))

fig.add_trace(go.Scatter(
    x=x, y=y,
    line_color='rgb(0,100,80)',
    name = "Puente Piedra<br>(Municipalidad)" 
))

fig.update_traces(mode='lines')

fig.update_layout(xaxis_title = "Frequencia (Hz)",
                      yaxis_title = "H/V",
                      title = "Espectro horizontal entre vertical (H/V)",
                      font = dict(size = 18)
                      ) 
        
# Configuraciones de diseño
fig.update_xaxes(ticks = "outside",
                 tickwidth = 1,
                 tickcolor = "black",
                 ticklen = 5,
                 showline=True,
                 linewidth=1,
                 linecolor='black',
                 mirror=True)
fig.update_yaxes(ticks = "outside",
                 tickwidth = 1,
                 tickcolor = "black",
                 ticklen = 5,
                 showline=True,
                 linewidth=1,
                 linecolor='black',
                 mirror=True)
fig.update_layout(template = "plotly_white")
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.95
))

fig.show()
