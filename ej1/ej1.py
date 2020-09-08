from itertools import combinations_with_replacement
import os
import sys

''' 
Uso: Llamamos a 
    $ python3 ej1.py [N que queremos usar]
Crea un archivo output_N.txt con todas las combinaciones posibles de largo N
con los caracteres a..z,0..9. Si no se pasa argumento se usa N = 4
'''

CHARS = "qwertyuiopasdfghjklñzxcvbnm123456789"
try:
    N = int(sys.argv[1])
except:
    print("No nos pasaron argumento N")
    N = 4
print(f"N es {N}")

if not os.path.isfile(f"./output_{N}.txt"):
    print("Archivo no existe, lo creamos")
    output = open(f"output_{N}.txt", 'w')
    output.write("[")
    for comb in combinations_with_replacement(CHARS, N):
        # Escribimos uno por uno en vez de crear una lista y escribirla entera
        # pq si no python se queda sin memoria
        output.write(f"'{''.join(comb)}',")
    output.write("]")
    output.close()
else:
    print("El archivo ya existe")
