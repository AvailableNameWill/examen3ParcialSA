arrEntrada = []
global tokenspos
global salida
global cant
#global texto
salida = ""
cant = 0
tokenspos = {}

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


texto = input('Ingrese la cadena')
salida = encriptar(texto)

print('salida:', salida)
print('longitud:', len(salida))



