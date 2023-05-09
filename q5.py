import pandas as pd
import matplotlib.pyplot as plt


alunos_df = pd.read_csv("alunos.csv")


gp_pais_separados_df = alunos_df[(alunos_df["escola"] == "GP") & (alunos_df["pais_separados"] == "Sim")]


media_tempo_estudo = gp_pais_separados_df["tempo_semanal_estudo"].mean()

print(f"A média do tempo semanal de estudo dos alunos cujos pais estão separados na escola GP é: {media_tempo_estudo:.2f} horas")



media_por_escola = alunos_df.groupby(["escola", "pais_separados"])["tempo_semanal_estudo"].mean()


media_por_escola.plot(kind="bar")


plt.xlabel("Escola e Pais Separados")
plt.ylabel("Tempo Semanal de Estudo (horas)")
plt.title("Média do Tempo Semanal de Estudo por Escola e Pais Separados")


plt.show()