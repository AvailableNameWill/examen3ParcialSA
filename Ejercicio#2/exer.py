arrEntrada = []
global tokenspos
global salida
global cant
global unknownChars
#global texto
salida = ""
cant = 0
tokenspos = {}
unknownChars = []

#texto = input('Ingrese la cadena')

path = 'text.txt'

dict = {}

with open(path, 'r') as file:
    for line in file:
        key, value = map(str.strip, line.split('='))

        dict[key] = value


# Función para encriptar la cadena
def encriptar(texto):
    global tokenspos
    global unknownChars
    resultado = []
    unknownChars = []
    for i, caracter in enumerate(texto):
        # Si el caracter está en el diccionario de encriptación, reemplazar, de lo contrario, usar 'N'
        encripted = dict.get(caracter, 'N')
        resultado.append(encripted)

        if encripted == 'N':
            unknownChars.append(caracter)
        else:
            tokenspos = {"posicion: ": i, "caracter: ": caracter}
    with open('noencriptados.txt', 'w') as noen:
        noen.write(''.join(unknownChars))

    return resultado


def desencript(encripted, unknown):
    decript = []

    for i, enchar in enumerate(encripted):
        if enchar == 'N' and unknown:
            decript.append(unknown.pop(0))
        else:
            decript.append(dict.get(enchar, enchar))
    return ''.join(decript)



texto = input('Ingrese la cadena')
salida = encriptar(texto)
original = desencript(salida, unknownChars)

print('salida:', salida)
print('longitud:', len(salida))
print(unknownChars)
print(original)



