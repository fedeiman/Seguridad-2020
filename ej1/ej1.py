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
    lists = list(combinations_with_replacement(CHARS, N))
    formattedlist = [''.join(tup) for tup in lists]
    with open(f"output_{N}.txt", 'w') as output:
        output.write(str(formattedlist))
else:
    print("El archivo ya existe")
