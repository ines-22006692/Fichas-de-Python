from os.path import join

def pede_nome ():
    i = 0
    while(i == 0):
        try:
            nome = input("Insira um nome:")
            f = open(nome)
            f.close()
            return nome
        except:
            print('O nome do ficheiro não existe')

def  gera_nome(nome,outro_argumento):
    nomeSeparado = nome.split(".")[0]
    o =".".join([nomeSeparado, 'json'])
    f = open(o ,"w")
    f.write(str (outro_argumento))
    f.close()



