#python 3

import angr 

p=angr.Project('./r1',auto_load_libs=False)

state=p.factory.entry_state()  

simgr=p.factory.simgr(state) 
#Direccion del Puts(puts("\nSuccess!! Too easy.");) que queremos ejecutar(en find)
#Direccion del Puts que no queremos ejecutar(en avoid)
res=simgr.explore(find=0x08048570,avoid=0x0804852d)    

print (res.found[0].posix.dumps(0)) 