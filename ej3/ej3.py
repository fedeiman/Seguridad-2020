import os
import glob 
import errno 

f = open("eko.txt","r") 
f1 = f.readlines()
ekodict = []
for i in range(len(f1)):
    ekodict.append(f1[i].replace('\n',''))

def checkifappear(path,ekodict):
    files = glob.glob(path) 
    wordlist = []
    for name in files: 
        with open(name) as f: 
            f2 = f.readlines()
            for i in range(len(f2)):
                wordlist.append(f2[i].replace('\n',''))
    appearWord = []

    for word in ekodict:
        if word in wordlist:
            appearWord.append(word)
    noApeear = set(ekodict) - set(appearWord)
    return(noApeear)
secList = checkifappear('/home/federico/Escritorio/SecLists/Passwords/*.txt',ekodict)
print(secList)
ns2 = checkifappear('/home/federico/Escritorio/ns2/*.txt',ekodict)
print(ns2)
