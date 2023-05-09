import pandas as pd
import plotly.express as px

alunos_df = pd.read_csv("alunos.csv")


saude_ms_atividades = alunos_df[(alunos_df["escola"] == "MS") & (alunos_df["atividades_extracurriculares"] == "sim")]["saude"]


desvio_padrao_saude_ms_atividades = saude_ms_atividades.std()

print(f"O desvio padrão do nível de saúde dos alunos da escola MS que frequentam atividades extracurriculares é: {desvio_padrao_saude_ms_atividades}")



saude_ms_atividades = alunos_df[(alunos_df["escola"] == "MS") & (alunos_df["atividades_extracurriculares"] == "sim")]["saude"]


fig = px.histogram(saude_ms_atividades, nbins=10)


fig.update_layout(xaxis_title="Nível de saúde", yaxis_title="Número de alunos", title="Distribuição do Nível de Saúde dos Alunos da Escola MS que Frequentam Atividades Extracurriculares")


fig.add_shape(type