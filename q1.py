
import pandas as pd
import matplotlib.pyplot as plt


alunos_df = pd.read_csv("alunos.csv")

media_idade = alunos_df["idade"].mean()

print(f"A média de idade dos alunos é: {media_idade:.2f} anos")

plt.bar(["Média de idade"], [media_idade])

plt.title("Média de idade dos alunos")
plt.xlabel("Dados")
plt.ylabel("Idade (anos)")

plt.show()