def encriptar(linea):

    if ord (linea) >=97 and ord(linea) < 122:
        return chr(ord(linea) + 1)

    if ord(linea) == 122:
        return 'a'
    else:
        return linea.upper()
archivo=open("jose_jose_quiereme.txt", 'r')
mensaje = archivo.read()
for mensaje in mensaje:
    print(encriptar(mensaje), end="")
archivo.close()
