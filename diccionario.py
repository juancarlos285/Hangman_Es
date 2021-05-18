
diccionario = []
with open('listado-general.txt') as vocabulario:
    for x in vocabulario:
        diccionario.append(x.lower().strip())
