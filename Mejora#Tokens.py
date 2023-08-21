import requests
from bs4 import BeautifulSoup
import re

# Función para preprocesar el texto
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Obtener el contenido de la página web
response = requests.get("https://www.eluniversal.com.mx/")
#print(response)
html_content = response.text
#print(html_content)
# Analizar el HTML de la página web
soup = BeautifulSoup(html_content, 'html.parser')

# Extraer el contenido de texto de la página
text_content = soup.get_text()
print(text_content)
# Guardar el contenido en un archivo
with open('parsed_text.txt', 'w', encoding='utf-8') as file:
    file.write(text_content)

# Preprocesar el contenido de texto
preprocessed_text = preprocess_text(text_content)

# Tokenizar el texto en palabras y caracteres individuales
word_tokens = preprocessed_text.split()
char_tokens = list(preprocessed_text)

# Imprimir los tokens en la consola
print("Tokens de palabras:")
print(word_tokens)
print("\nTokens de caracteres:")
print(char_tokens)