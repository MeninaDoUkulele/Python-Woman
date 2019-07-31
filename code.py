
# Importando biblioteca json
import json



'''-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-'''
''' NOTES '''
'''
| 1 | - Construção do arquivo json

    len(jsonFile) -> 7
    jsonFile[0] -> {
    jsonFile[1] -> "numero_casas":12,
    jsonFile[2] -> "token":"583e2c39c3c48ff7ba43dfbebfa1c2f0e831788c",
    jsonFile[3] -> "cifrado":"bdasdmyyuzs xmzsgmsqe, xuwq bullme, oayq 
                    uz azxk fia eulqe: faa nus mzp faa eymxx. duotmdp bmffue",
    jsonFile[4] -> "decifrado":"",
    jsonFile[5] -> "resumo_criptografico":""
    jsonFile[6] -> }
'''
'''
| 2 | - Funções que podem ajudar

    .lower() -> minusculo
'''

# help = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
help = 'abcdefghijklmnopqrstuvwxyz'


# Função que abre o arquivo
def openJson():
    # Lendo aquivo json
    file = open('answer.json', 'r')
    # Preenchendo o vetor jsonFile, cada linha um espaço do vetor
    jsonFile = file.readlines()

    # Fechando arquivo de leitura
    file.close()
    return jsonFile

def find(letter):
    position = help.find(letter) - 12
    return help[position]

def operation(letter):
    if 'z' >= letter >= 'm': return chr(ord(letter) - 12)
    elif 'l' >= letter >= 'a': return find(letter)
    else: return letter

def decryption(text):
    if len(text) == 0: return text
    else: return operation(text[0]) + decryption(text[1:])

# Função principal
def main():
    # Obtendo o vetor com o arquivo através da chamada de função
    jsonFile = openJson()

    # jsonFile[3]
    # return decryption(?)

    
    
        

txt = 'bdasdmyyuzs'
txt2 = 'bdasdmyyuzs xmzsgmsqe, xuwq bullme, oayq uz azxk fia eulqe: faa nus mzp faa eymxx. duotmdp bmffue'

print(decryption(txt2))
# print(find('l'))
