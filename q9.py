import pandas as pd
import plotly.graph_objects as go

alunos_df = pd.read_csv("alunos.csv")


num_alunos_cumpriram_horas = alunos_df[alunos_df["horas_extracurriculares_cumpridas"] > 0].shape[0]

print(f"O número de alunos que já cumpriram as horas extracurriculares é: {num_alunos_cumpriram_horas}")


num_alunos_cumpriram_horas = alunos_df[alunos_df["horas_extracurriculares_cumpridas"] > 0].shape[0]


fig = go.Figure(go.Bar(x=["Alunos com horas extracurriculares cumpridas", "Alunos sem horas extracurriculares cumpridas"], y=[num_alunos_cumpriram_horas, alunos_df.shape[0] - num_alunos_cumpriram_horas]))


fig.update_layout(xaxis_title="", yaxis_title="Número de alunos", title="Distribuição dos Alunos por Horas Extracurriculares Cumpridas")


fig.show()