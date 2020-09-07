f = open("10-million-password-list-top-100.txt","r") 
f1 = f.readlines()
largo = []
for i in range(len(f1)):
    largo.append(len(f1[i].replace('\n','')))

print 'Longitud mas frecuente', max(set(largo), key = largo.count)

cutstr = []
digits = []
for x in f1:
    cutstr.append(x.replace('\n','')[-4:])

for x in cutstr:
    if x.isdigit():
        #a = int(x)
        digits.append(x)
cutstr = []

for _ in range(0,10):
    cutstr.append(max(set(digits), key = digits.count))
    digits = list(filter(lambda x : x != (max(set(digits), key = digits.count)), digits))  
print '10 sufijos de digitos mas usados',cutstr