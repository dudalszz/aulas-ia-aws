# Desafio
# Criar um programa para verificar se uma frase é um palíndramo

def is_palindramo(texto):
    texto_limpo = ''.join(char.lower()
                          for char in texto 
                          if char.isalnum())
    return texto_limpo == texto_limpo[:: -1]

frase = "anotaram a data da maratona"
resultado = is_palindramo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{frase}' é um palindramo? {resposta}")