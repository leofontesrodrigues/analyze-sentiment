import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')

def limpar_texto(texto):
    # Remover pontuação e números
    texto = ''.join([char for char in texto if char not in string.punctuation])
    texto = ''.join([char for char in texto if not char.isdigit()])
    
    # Converter para minúsculas
    texto = texto.lower()

    # Remover stopwords
    stop_words = set(stopwords.words('portuguese'))  # ou 'english', dependendo do idioma
    palavras = texto.split()
    palavras_limpa = [palavra for palavra in palavras if palavra not in stop_words]
    
    return ' '.join(palavras_limpa)
