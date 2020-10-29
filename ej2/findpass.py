password = ''
for i in range(len('5tr0vZBrX:xTyR-P!')):
    password = password + chr((i ^ ord('5tr0vZBrX:xTyR-P!'[i])))

print(password)