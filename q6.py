import pandas as pd
import plotly.express as px


alunos_df = pd.read_csv("alunos.csv")


moda_motivo_escolha = alunos_df[alunos_df["escola"] == "MS"]["motivo_escolha"].mode()[0]

print(f"A moda do motivo pelo qual os alunos escolheram a escola MS é: {moda_motivo_escolha}")



contagem_por_motivo = alunos_df[alunos_df["escola"] == "MS"].groupby("motivo_escolha").size().reset_index(name="contagem")


fig = px.pie(contagem_por_motivo, values="contagem", names="motivo_escolha")


fig.update_layout(title="Moda do Motivo pelo qual os Alunos Escolheram a Escola MS")


fig.show()