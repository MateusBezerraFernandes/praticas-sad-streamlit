from statistics import mode
import plotly.graph_objects as go



moda_endereco = mode(endereco_alunos)

print(f"A moda do endereço dos alunos é: {moda_endereco}")


contagem_endereco = {endereco: endereco_alunos.count(endereco) for endereco in endereco_alunos}


moda_endereco = max(contagem_endereco, key=contagem_endereco.get)


fig = go.Figure(data=[go.Pie(labels=list(contagem_endereco.keys()), values=list(contagem_endereco.values()))])


fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=[('red' if endereco == moda_endereco else 'grey') for endereco in contagem_endereco.keys()],
                              line=dict(color='#FFFFFF', width=2)))

fig.update_layout(title="Moda do endereço dos alunos")
fig.show()