import csv
import os
from matplotlib import pyplot as plt


def pede_pasta():
    i = 0
    while (i == 0):
        try:
            caminho = input("Inserir um caminho para uma pasta:")
            if os.listdir(caminho):
                return caminho

        except:
            print('O caminho para uma pasta não existe')

def faz_calculos(path):

    if not os.path.exists(path):
        print('Pasta não foi encontrada')
        return None

    dicionario = dict()

    for i in os.listdir(path):
        tamanho = os.path.getsize(path + '\\' + i)

        separado = i.split(".", 2)


        if separado[1] in dicionario:
            dicionario[separado[1]]['volume'] += tamanho
            dicionario[separado[1]]['quantidade'] += 1
        else:
            dicionario[separado[1]] = dict()
            dicionario[separado[1]]['volume'] = tamanho
            dicionario[separado[1]]['quantidade'] = 1

    return separado

def guarda_resultados(path, dic_info):

    if not os.path.exists(path):
        print('A informação não foi criada')
        return None

    if dic_info == None:
        print('A informação não foi criada')
        return None

    nome = path.split("\\")[-1] + ".csv"

    with open(nome, 'w', newline='') as file:
        escrito = csv.writer(file)
        escrito.writerow(["Extensao"," Quantidade"," Tamanho[kByte]"])

        for tipo,informacao in dic_info.items():
            escrito.writerow([type, informacao['quantidade'], informacao['volume']])

    return (f"Os resultados foram guardados no ficheiro '{nome}'.")

def faz_grafico_queijos(dic_info):

    data = list()
    quantidade = list()
    for type, info in dic_info.items():
        data.append(type)
        quantidade.append(info['quantidade'])

    plt.pie(quantidade, labels=data, startangle=90, autopct='%1.1f%%')
    plt.title("Quantidade não foi encontrada")
    plt.tight_layout()
    plt.show()

def faz_grafico_barras(dic_info):


    data = list()
    quantidade = list()
    for tipo, informacao in dic_info.items():
        tipo.append(type)
        quantidade.append(informacao['volume'])

    plt.bar(tipo, quantidade)
    plt.title("Quantidade de Bytes")
    plt.show()



