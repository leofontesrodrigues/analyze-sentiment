import matplotlib.pyplot as plt
from collections import Counter

def gerar_grafico(sentimentos):
    # Contagem dos sentimentos
    contagem = Counter(sentimentos)
    labels, valores = zip(*contagem.items())

    # Criar gráfico de barras
    plt.bar(labels, valores)
    plt.title('Distribuição de Sentimentos')
    plt.xlabel('Sentimentos')
    plt.ylabel('Número de Ocorrências')
    plt.savefig('outputs/distribuicao.png')  # Salvar o gráfico
    plt.show()
