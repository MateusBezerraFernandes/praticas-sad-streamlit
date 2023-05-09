import pandas as pd


alunos_df = pd.read_csv("alunos.csv")


ms_com_apoio_df = alunos_df[(alunos_df["escola"] == "MS") & (alunos_df["apoio_educacional_extra"] == "Sim")]


desvio_padrao_idade = ms_com_apoio_df["idade"].std()

print(f"O desvio padrão da idade dos alunos que têm apoio educacional extra na escola MS é: {desvio_padrao_idade:.2f} anos")


desvio_padrao_por_escola = alunos_df.groupby(["escola", "apoio_educacional_extra"])["idade"].std()


print(desvio_padrao_por_escola)