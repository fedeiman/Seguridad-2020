import collections

f = open("10-million-password-list-top-100.txt","r") 
f1 = f.readlines()
largo = []
for i in range(len(f1)):
    largo.append(len(f1[i].replace('\n','')))

print 'Longitud mas recuente', max(set(largo), key = largo.count)

cutstr = []
digits = []
for x in f1:
    cutstr.append(x.replace('\n','')[-4:])

for x in cutstr:
    if x.isdigit():
        digits.append(x)
        
print '10 sufijos de digitos mas usados',collections.Counter(digits).most_common(10)
