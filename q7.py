import pandas as pd
import matplotlib.pyplot as plt

alunos_df = pd.read_csv("alunos.csv")


mediana_faltas_gp = alunos_df[alunos_df["escola"] == "GP"]["faltas"].median()

print(f"A mediana do número de faltas dos alunos que frequentam a escola GP é: {mediana_faltas_gp}")


faltas_gp = alunos_df[alunos_df["escola"] == "GP"]["faltas"]


plt.hist(faltas_gp, bins=20)


plt.xlabel("Número de faltas")
plt.ylabel("Número de alunos")


plt.axvline(mediana_faltas_gp, color='r', linestyle='dashed', linewidth=1)


plt.title("Distribuição do Número de Faltas dos Alunos da Escola GP")


plt.show()