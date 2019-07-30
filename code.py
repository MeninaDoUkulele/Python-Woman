
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


# Função que abre o arquivo
def openJson():
    # Lendo aquivo json
    file = open('answer.json', 'r')
    # Preenchendo o vetor jsonFile, cada linha um espaço do vetor
    jsonFile = file.readlines()

    # Fechando arquivo de leitura
    file.close()
    return jsonFile

# Função principal
def main():
    # Obtendo o vetor com o arquivo através da chamada de função
    jsonFile = openJson()

    for line in jsonFile :
        print(line)
        



