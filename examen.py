from pprint import pprint

def get_list(fichero):
    dic = {}
    cont = 1
    f = open(fichero, mode="rt", encoding="utf-8")
    linea = f.readline()
    if linea == "":
        f.close()
        raise ValueError("El fichero esta vacio")
    for linea in f:
        print("he leído: " + str(len(linea)-1))
        array = []
        if len(linea)-1:
            
        dic[len(linea)-1] = [linea]

    f.close()
    return dic

res = get_list("palabras.txt")
pprint(res)