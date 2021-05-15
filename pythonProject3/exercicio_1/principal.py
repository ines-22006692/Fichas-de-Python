from exercicio_1.analisa_ficheiro import *
from exercicio_1.analisa_ficheiro.acessorio import pede_nome, gera_nome
from exercicio_1.analisa_ficheiro.calculos import calcula_linhas, calcula_carateres, calcula_palavra_comprida, \
    calcula_ocorrencia_de_letras


def main():
    outro = {}
    nome = pede_nome()
    gera_nome(nome,outro)
    calcula_linhas(nome)
    calcula_carateres(nome)
    calcula_palavra_comprida(nome)
    calcula_ocorrencia_de_letras(nome)


if __name__ == "__main__":
    main()