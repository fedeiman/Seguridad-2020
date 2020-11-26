# Escalera Pedro, Iman Federico

#### Ej 3
Un análisis forense es tremendamente útil la obtención del volcado de memoria volátil y su posterior análisis, sobretodo porque muchos artefactos de malware usan funciones que no dejan datos en disco.

Las herramientas mas comunes y conocidas para la extraccion y analisis de memoria en linux son: 

1. Volatility Framework: quizás una de las más famosas colecciones de herramientas para la extración y el análisis de la memoria volatil (RAM). Sin embargo el soporte para Linux es todavía experimental: ver la página LinuxMemoryForensics en el Volatility wiki. (Licencia GNU GPL)

2. LiME (Linux Memory Extractor): presentado en la ShmooCon 2012, es un módulo cargable para el kernel (LKM) y permite la adquisión de memoria incluso en Android.

3. Draugr: interesante herramienta que puede buscar símbolos del kernel (patrones en un fichero XML o con EXPORT_SYMBOL), procesos (información y secciones) (por la lista de enlaces del kernel o por fuerza bruta) y desensamblar/volcar la memoria.

4. Volatilitux: framework en Python equivalente a Volatility en Linux. Soporta arquitecturas ARM, x86 y x86 con PAE activado.

5. Memfetch: sencilla utilidad para volcar la memoria de procesos en ejecución o cuando se descubre una condición de fallo (SIGSEGV).

6. Crash utility from Red Hat, Inc: es una herramienta independiente para investigar tanto los sistemas en funcionamiento como los volcados de memoria del kernel hechos con lo paquetes de Red Hat netdump, diskdump o kdump. También se puede utilizar para el análisis forense de memoria.

7. Memgrep: sencilla utilidad para buscar/reemplazar/volcar memoria de procesos en ejecución y ficheros core.

8. Memdump: se puede utilizar para volcar la memoria del sistema al stream de salida, saltando los huecos de los mapas de la memoria. Por defecto vuelca el contenido de la memoria física (/dev/mem). Se distribuye bajo la Licencia Pública de IBM.

9. Foriana: esta herramienta es útil para la extracción de información de procesos y listas de módulos desde una imagen de la RAM con la ayuda de las relaciones lógicas entre las estructuras del sistema operativo.

11. Forensic Analysis Toolkit (FATKit): un nuevo framework multiplataforma y modular diseñado para facilitar la extracción, análisis, agregación y visualización de datos forenses en varios niveles de abstracción y complejidad de datos.

12. The Linux Memory Forensic Acquisition (Second Look): esta herramienta es una solución comercial con un driver de crashing modificado y scripts para volcado.

[Fuente](https://www.cyberciti.biz/programming/linux-memory-forensics-analysis-tools/)

Luego para realizar el dumpeo de memoria, decidimos usar la maquina virtual de kali linux instalada en el practico 1.
Utilizamos la herramienta Lime
Lo primero que hicimos fue instalar lime en kali, y averiguar la direccion ip de la maquine virtual, ya que enivaremos por tcp el dump de la memoria.

![fs](Screenshot_2020-11-26_16-39-34.png)

una vez hecho esto, nos pusimos en nuestra maquina local, a escuchar con netcat

![fs](Selection_002.png)

Una vez hecho esto, conseguimos el archivo kali.mem con el dump de memoria, el cual se encuentra disponible para descargar en este [link](https://drive.google.com/file/d/1Q-d86X4v9o_zB_7bYYy9JPzQ5j-qZS2R/view?usp=sharing).

#### Ej 4


Ahora, para realizar un dumpeo de memoria

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