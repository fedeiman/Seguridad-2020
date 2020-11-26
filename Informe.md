# Escalera Pedro, Iman Federico

#### Ej 4


Utilizamos la herramienta Recuva de windows para recuperar los archivos, es una herramienta muy simple de usar en que para nuestro caso funciono perfecto con los 3 archivos que intentamos recuperar.

![Texto alternativo](Captura.PNG)
![Texto alternativo](1.PNG)

Una vez recuperados los archivos pasamos a intentar crackear las password de fsecret_doc.docx

Para esto investigamos un poco en internet las herramientas nombradas en el ejercio y encontramos el siguiente [link](https://byte-mind.net/crackear-documentos-office-protegidos-con-contrasena/)
El cual nos muestra una herramienta para obtener el hash llamada Office2John y corrieno el comando: 

    python office2john.py fsecret_doc.docx > hash.txt

obtenemos el siguiente hash:

    fsecret_doc.docx:$office$*2007*20*128*16*ba1ae53b4d016fc3a15124b2a3034779*49a69de2853eac6c62cceeeb549aac18*57e5fd8bfd182b4c70071a3052b91194e048055c


una vez obtenido el hash, usamos la herramienta hashcat que ya bien conocemos. Primero realizando ataques con el dicionario 1 sin resultados, luego con el 2, nuevamente sin resultados, y finalmente con una convinacion de ambos usando el siguiente comando:

    hashcat -a 1 -m 9400 --username hash.txt diccionario1.txt diccionario2.txt 

y obteniendo como resultado la clave: 

    jimmyisno.1saop91

Aclaracion: el Link antes citado dice que a el hash obtenido debemos borrarle el incio (nombre del archivo y los :) Pero esto no es verdad, ya que eliminando esto hashcat no reconoce el hash por lo que no hay que editar el hash obtenido con office2john.py