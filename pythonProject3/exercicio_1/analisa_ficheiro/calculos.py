import os
import sys


def calcula_linhas(nome):
    count = 0
    f = open(nome, "r")
    for i in f:
        count = count + 1
    f.close()

def calcula_carateres(nome):
    count = 0
    f = open(nome)
    ficheiro = f.read()
    for i in ficheiro.split():
        count += len(i)
    f.close()
    return count
def calcula_palavra_comprida(nome):
    count = 0
    word = ""
    f = open(nome)
    ficheiro = f.read()
    for i in ficheiro.split():
        if len(i) > count:
            count = len(i)
            word = i
    f.close()
    return word

def calcula_ocorrencia_de_letras(nome):
    dicionario = {}
    f = open(nome)
    ficheiro = f.read()
    for i in set(ficheiro):
        if i != '\n':
            dicionario[i] = ficheiro.count(i)
    f.close()
    return dicionario


