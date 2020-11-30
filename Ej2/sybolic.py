from manticore.native import Manticore

m = Manticore('./r1')
m.context['flag'] = ""

#Direccion a la que queremos llegar?
@m.hook(0x08048569)
def hook(state):
    cpu = state.cpu
    #Direccion del buffer con respecto al basepointer pero no le tengo confianza, lo busque en gdb...
    transform_base = cpu.RBP - 0x44
    #la rta tiene 17 bytes ( 17 chars)
    for i in range(17):
        solved = state.solve_one(cpu.read_int(transform_base + i, 8))
        print(solved)
        m.context['flag'] += chr(solved)
    print(m.context['flag'])
    m.terminate()

m.run()