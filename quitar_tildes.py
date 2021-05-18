def quitar_tildes(palabra):
    vocales_tildadas = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    sin_tildes = ""
    for x in palabra:
        if x in vocales_tildadas:
            x = vocales_tildadas[x]
            sin_tildes += x
        else:
            sin_tildes += x
    return sin_tildes