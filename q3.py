import pandas as pd
import matplotlib.pyplot as plt


alunos_df = pd.read_csv("alunos.csv")


mediana_tempo_gp = alunos_df[alunos_df["escola"] == "GP"]["tempo_de_viagem"].median()

print(f"A mediana do tempo de viagem dos alunos da escola GP é: {mediana_tempo_gp:.2f} minutos")




plt.plot(["Mediana do tempo de viagem"], [mediana_tempo_gp])


plt.title("Mediana do tempo de viagem dos alunos da escola GP")
plt.xlabel("Dados")
plt.ylabel("Tempo de viagem (minutos)")


plt.show()