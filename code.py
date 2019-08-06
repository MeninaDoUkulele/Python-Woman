
# Importando biblioteca json
import json
import hashlib



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
    with open('text.json', 'r') as myfile:
        data = myfile.read()
    
    jsonFile = json.loads(data)
    return [jsonFile['numero_casas'],jsonFile['cifrado'],jsonFile['token']]

def closeJson(decrypted):
    with open('text.json', 'w') as outfile:
        # json.dump(decrypted, outfile)
        json.dumps({'decifrado': decrypted}, sort_keys=True, separators=(',', ': '))

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

    shaUm = hashlib.sha1()
    shaUm.update(decrypted.encode("utf-8"))
    encriptado = shaUm.hexdigest()


if __name__ == '__main__':
    main()

txt2 = 'bdasdmyyuzs xmzsgmsqe, xuwq bullme, oayq uz azxk fia eulqe: faa nus mzp faa eymxx. duotmdp bmffue'

# print(decryption(txt2))
# print(find('l'))
