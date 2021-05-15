import os


def pede_pasta():
    i = 0
    while (i == 0):
        try:
            caminho = input("Inserir um caminho para uma pasta:")
            if os.listdir(caminho):
                return caminho

        except:
            print('O caminho para uma pasta não existe')

def calcula_tamanho_pasta(pasta):
    soma = 0;
    for i in pasta:
        resultado = os.path.join(pasta, i)
        if os.path.isfile(resultado):
            soma += (os.path.getsize(resultado) /1048576 )

        if os.path.isdir(resultado):
            soma += calcula_tamanho_pasta(i)

    return soma

def main():
    pasta = pede_pasta()
    calcula_tamanho_pasta(pasta)

if __name__ == "__main__":
    main()