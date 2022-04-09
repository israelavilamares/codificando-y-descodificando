def encriptar(linea):

    if ord(linea) >= 97 and ord(linea) < 122:
        return chr(ord(linea) + 1)

    if ord(linea) == 122:
        return 'z'
    else:
        return linea.upper()

def desencriptar(linea):

    if ord(linea) >= 97 and ord(linea) < 123:
        return chr(ord(linea) - 1)

    if ord(linea) == 97:
        return 'z'
    else:
        return linea.upper()

archivo=open("jose_jose_quiereme.txt", 'r')
filecodi=open("codificadojose_jose_quiereme.txt", 'w')
mensaje = archivo.read()
for mensaje in mensaje:
    filecodi.write(encriptar(mensaje))
archivo.close()
filecodi.close()

filecodi=open("codificadojose_jose_quiereme.txt", 'r')
filedescodificar=open("descodificadojose_jose_quiereme.txt", 'w')
cancion=filecodi.read()
for cancion in cancion:
    filedescodificar.write(desencriptar(cancion))
filecodi.close()
filedescodificar.close()

archivo=open("jose_jose_quiereme.txt", 'r')
archivoriginal=archivo.read()
filedescodificar=open("descodificadojose_jose_quiereme.txt", 'r')
descodificado=filedescodificar.read()
archivo.close()
filedescodificar.close()
if archivoriginal==filedescodificar:
    print("la comparacion del los dos archivos son iguales el original el descodificar")
else:
    print("son diferentes los archivos comparados el original y el descodificar")
