# Análise de Sentimentos com Azure AI

Este projeto foi desenvolvido para realizar a análise de sentimentos de um conjunto de sentenças utilizando o **Language Studio da Microsoft Azure**. A análise de sentimentos pode ser aplicada para entender as opiniões expressas em textos, como feedbacks de usuários, resenhas de produtos ou posts em redes sociais.

---

## :rocket: Como Funciona

O projeto realiza a análise de sentimentos seguindo os seguintes passos:

1. **Carregar um arquivo de texto** com várias sentenças.
2. **Utilizar a API de Sentiment Analysis do Azure** para classificar o sentimento de cada sentença como:
   - `Positivo`
   - `Negativo`
   - `Neutro`
3. **Exibir os resultados** no console e gerar um gráfico de distribuição de sentimentos.

---

## :hammer_and_wrench: Como Usar

Siga os passos abaixo para rodar o projeto:

1. **Crie uma conta no Azure**:
   - Acesse [Azure Portal](https://portal.azure.com/) e crie uma conta caso não tenha uma.
   
2. **Crie um recurso de Language Service no Azure**:
   - Vá para o portal do Azure, crie um novo recurso e busque por "Language Service".
   - Obtenha a chave e o endpoint gerados para configuração no script Python.

3. **Configure o script Python**:
   - No arquivo `src/sentiment_analysis.py`, insira a chave e o endpoint da sua conta do Azure.

4. **Prepare o arquivo de entrada**:
   - Coloque as sentenças a serem analisadas no arquivo `inputs/sentencas.txt`.

5. **Execute o script Python**:
   - Execute o script:
     ```bash
     python src/sentiment_analysis.py
     ```

6. **Verifique os resultados**:
   - Os resultados serão exibidos no console e o gráfico gerado será salvo na pasta `outputs`.

---

## :bar_chart: Resultados e Insights

Durante o processo de análise, podemos observar que a API de Sentiment Analysis do Azure fornece insights valiosos sobre o feedback dos usuários. Algumas possíveis aplicações incluem:

- **Análise de resenhas de produtos**: Para entender a opinião dos consumidores sobre um produto ou serviço.
- **Monitoramento de redes sociais**: Para identificar a percepção pública sobre uma marca, evento ou tópico específico.
- **Pesquisa de mercado**: Para avaliar o sentimento em relação a campanhas publicitárias ou lançamentos de novos produtos.

Aqui está um exemplo de saída:

```bash
Sentença: "Eu adoro este produto!"
Sentimento: Positivo

Sentença: "Estou muito insatisfeito com o serviço."
Sentimento: Negativo
