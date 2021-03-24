from pprint import pprint

def get_list(fichero):
    dic = {}
    cont = 1
    f = open(fichero, mode="rt", encoding="utf-8")
    linea = f.readline()
    if linea == "":
        f.close()
        raise ValueError("El fichero esta vacio")
    while linea != "" :
        dic[cont] = []
        if (cont == len(linea)-1):
            dic[cont]
        linea = f.readline()
        cont=cont+1
    f.close()
    return dic

res = get_list("palabras.txt")
pprint(res)