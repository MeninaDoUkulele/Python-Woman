
# Importando biblioteca json
import json



'''-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-'''
''' NOTES '''
'''
| 1 | - Funções que podem ajudar

    .lower() -> minusculo
'''

# help = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
help = 'abcdefghijklmnopqrstuvwxyz'


# Função que abre o arquivo
def openJson():
    with open('answer.json', 'r') as myfile:
        data = myfile.read()
    
    jsonFile = json.loads(data)
    return [jsonFile['numero_casas'],jsonFile['cifrado']]

    

def find(letter, key):
    position = help.find(letter) - key
    return help[position]

def operation(letter, key):
    if 'z' >= letter >= 'm': return chr(ord(letter) - key)
    elif 'l' >= letter >= 'a': return find(letter, key)
    else: return letter

def decryption(text, key):
    if len(text) == 0: return text
    else: return operation(text[0], key) + decryption(text[1:], key)

# Função principal
def main():
    # Obtendo o vetor com o arquivo através da chamada de função
    jsonFile = openJson()

    decrypted = decryption(jsonFile[1], jsonFile[0])

    return decrypted
    
        

txt = 'bdasdmyyuzs'
txt2 = 'bdasdmyyuzs xmzsgmsqe, xuwq bullme, oayq uz azxk fia eulqe: faa nus mzp faa eymxx. duotmdp bmffue'

# print(decryption(txt2))
# print(find('l'))
