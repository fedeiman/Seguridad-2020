# Escalera Pedro, Iman Federico

  

### Ej 1

  

#### Red a escanear: https://www.famaf.unc.edu.ar/

  
  

Lo primero que hicimos fue correr

    dnsenum https://www.famaf.unc.edu.ar

  

Cuando dnsenum realizo fuerza bruta sobre el archivo dns.txt encontró unos cuantos dns pero entre todo lo que nos dio encontramos información importante como la siguiente:

  

    www.famaf.unc.edu.ar. 128 IN CNAME ratri.famaf.unc.edu.ar.

  

Lo que significa que www.famaf.unc.edu.ar es un alias para el nombre de dominio ratri.famaf.unc.edu.ar y justo abajo de esto, dnsenum no devuelve la ip de ratri.famaf.unc.edu.ar es decir la ip de www.famaf.unc.edu.ar

  

    ratri.famaf.unc.edu.ar. 127 IN A 200.16.17.123

  

por ende famaf tiene la ip 200.16.17.123 y es de tipo a.

  

Algunos de los dns obtenidos con dnsenum fueron:

  

* eolo.famaf.unc.edu.ar.

  

* pop.famaf.unc.edu.ar.

  

* agni.famaf.unc.edu.ar.

  

* server.famaf.unc.edu.ar.

  

* isis.famaf.unc.edu.ar.

  

* smtp.famaf.unc.edu.ar.

  

* agni.famaf.unc.edu.ar.

  

* webmail.famaf.unc.edu.

  

* www.famaf.unc.edu.ar.

  

* ratri.famaf.unc.edu.ar.

  

* www2.famaf.unc.edu.ar.

  

* ra.famaf.unc.edu.ar.

  

Una vez realizada esta prueba pasamos a hacer un escaneo de puertos usando nmap y algunas flags interesantes para obtener mas información.

  

Corriendo:

  

    sudo nmap -O 200.16.17.123 -sV

  

obtuvimos la siguiente información:

  

    Not shown: 997 filtered ports

    

    PORT STATE SERVICE VERSION

    

    22/tcp open ssh OpenSSH 7.4p1 Debian 10+deb9u7 (protocol 2.0)

    

    80/tcp open http nginx 1.10.3

    

    443/tcp open ssl/http nginx 1.10.3

    

    Device type: general purpose

    

    Running: Linux 3.X|4.X

    

    OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4

    

    OS details: Linux 3.10 - 4.11, Linux 3.16 - 4.6, Linux 3.2 - 4.9

    

    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

  

Analizando esta información, parece que hay 3 puertos abiertos 2 con una versión de nginx

y el 3ero con debian.

  

Ademas, el sistema operativo es Linux Linux 3.X|4.X

  

Corriendo whatweb obtuvimos una confirmación de que el ip de famaf es 200.16.17.123 y que están usando javascript pero no mucho mas.

Usando la herramienta dirb no pudimos encontrar o listar ningún endpoint.

  

Finalmente usando el servicio web https://hostingchecker.com/ encontramos otra información como el nombre de la organización y la ubicación del ip.