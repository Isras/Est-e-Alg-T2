def separarultimageracao(diretorio):
    pais = []
    filhoseterras = []
    with open(diretorio, "r") as pergaminho:
        next(pergaminho)
        for line in pergaminho:
            pai, filho = line.split(" ", 1)
            if pai in pais:
                i = 1
            else:
                pais.append(pai)
            
            if filho in filhoseterras:
                i += 1
            elif filho in pais:
                i += 1
            else:
                filhoseterras.append(filho)

    for elemento in filhoseterras:
        nomedofilho, quantiaterras = elemento.split(" ")
        if nomedofilho in pais:
            filhoseterras.remove(elemento)

def encontraralvo():
    


separarultimageracao("casosdeteste/caso10c.txt")