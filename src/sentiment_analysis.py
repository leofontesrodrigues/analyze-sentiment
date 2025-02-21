from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from text_preprocessing import limpar_texto
from visualize import gerar_grafico

key = "<sua_chave>"
endpoint = "<seu_endpoint>"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def analisar_sentimento(texto):
    response = client.analyze_sentiment([texto])
    return response[0].sentiment

def processar_sentencas(input_file):
    sentimentos = []
    with open(input_file, "r") as file:
        for linha in file:
            texto_limpo = limpar_texto(linha)
            sentimento = analisar_sentimento(texto_limpo)
            sentimentos.append(sentimento)
    return sentimentos

if __name__ == "__main__":
    sentimentos = processar_sentencas("inputs/sentencas.txt")
    gerar_grafico(sentimentos)
