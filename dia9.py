frase = input("Introduce una frase: \n")

caracteres = len(frase)
espacios = 0
vocales = 0
consonantes = 0
numeros = 0
otros = 0
detalle_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for caracter in frase:
    if caracter == " ":
        espacios += 1
    elif caracter in "aeiouáéíóúAEIOUÁÉÍÓÚ":
        vocales += 1
    elif caracter in "bBcCdDfFgGhHjJkKlLmMnNñÑpPqQrRsStTvVwWxXyYzZ":
        consonantes += 1
    elif caracter in "1234567890":
        numeros += 1
    else:
        otros += 1

    if caracter in "aAáÁ":
        detalle_vocales["a"] += 1
    elif caracter in "eEéÉ":
        detalle_vocales["e"] += 1
    elif caracter in "iIíÍ":
        detalle_vocales["i"] += 1
    elif caracter in "oOóÓ":
        detalle_vocales["o"] += 1
    elif caracter in "uUúÚ":
        detalle_vocales["u"] += 1
    
print(f"""\nCaracteres : {caracteres}
Espacios: {espacios}
Vocales: {vocales}
Vocal 'a': {detalle_vocales['a']}
Vocal 'e': {detalle_vocales['e']}
Vocal 'i': {detalle_vocales['i']}
Vocal 'o': {detalle_vocales['o']}
Vocal 'u': {detalle_vocales['u']}
Consonantes: {consonantes}
Números: {numeros}
Otros: {otros}""")


frase_invertida = ""
print("Frase invertida: ", end="")
for caracter in range (len(frase) -1, -1, -1):
    print(frase[caracter], end="")
    frase_invertida += frase[caracter]

if frase_invertida == frase:
    print("La frase SI es un palíndromo")
else:
    print("La frase NO es un palíndromo")