archivo=open("jose_jose_quiereme.txt",'r')
lines=archivo.readlines()
for lines in lines:
    print(lines.strip())
    line = archivo.readline()

archivo.close()