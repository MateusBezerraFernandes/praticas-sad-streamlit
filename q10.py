import pandas as pd
import plotly.graph_objects as go

alunos_ms_df = pd.read_csv("alunos_ms.csv")


moda_consumo_alcool_semana_trabalho = alunos_ms_df["consumo_alcool_semana_trabalho"].mode()[0]

print(f"A moda do consumo de álcool dos alunos da escola MS durante a semana de trabalho é: {moda_consumo_alcool_semana_trabalho}")



moda_consumo_alcool_semana_trabalho = alunos_ms_df["consumo_alcool_semana_trabalho"].mode()[0]


fig = go.Figure(data=[go.Table(header=dict(values=["Consumo de álcool durante a semana de trabalho"]),
                 cells=dict(values=[[moda_consumo_alcool_semana_trabalho]]))])

fig.show()