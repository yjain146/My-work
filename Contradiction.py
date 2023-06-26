def notlist(p):
    notp=[]
    for i in range(len(p)):
        if p[i]==True:
            notp.append(False)
        else:
            notp.append(True)
    return notp

p=[True, True, False, False]

notp=[]

notp=notlist(p)
cont=[]

for i in range(len(p)):
    if (p and notp)==True:
        cont.append(True)
    else:
        cont.append(False)

flag=0
for i in range(len(cont)):
    if cont[i]==False:
        continue
    else:
        flag=1

if flag==0:
    print("Contradiction found")
    for i in range(len(cont)):
        print(cont[i], "\n")
else:
    print("Contradiction not found")