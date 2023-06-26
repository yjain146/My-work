def pimpliesq(p,q):
    pq=[]
    for i in range(len(p)):
        if p[i]==True and q[i]==False:
            pq.append(False)
        else:
            pq.append(True)
    return pq

def pandq(p,q):
    pandq=[]
    for i in range(len(p)):
        if (p[i] and q[i]) == True:
            pandq.append(True)
        else:
            pandq.append(False)

def porq(p,q):
    for i in range(len(p)):
        if (p[i] or q[i]) == True:
            porq.append(True)
        else:
            porq.append(False)

def notlist(p):
    notp=[]
    for i in range(len(p)):
        if p[i]==True:
            notp.append(False)
        else:
            notp.append(True)
    return notp

p=[True, True, False, False]
q=[True, False, True, False]

notp=[]
notq=[]
pq=[]
notqp=[]
taut=[]
cont=[]

notp=notlist(p)
notq=notlist(q)

pq=pimpliesq(p,q)
notqp=pimpliesq(notq,notp)

taut=pimpliesq(pq,notqp)
cont=pandq(p,notp)


flag=0
for i in range(len(taut)):
    if taut[i]==True:
        continue
    else:
        flag=1

if flag==0:
    print("Tautology found")
    for i in range(len(taut)):
        print(taut[i], "\n")
else:
    print("Tautology not found")