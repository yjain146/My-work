a=[]
b=[]
f= int(input("Enter the number of digits you want for the First set: "))
h= int(input("Enter the number of digits you want for the Second set: "))
for i in range(f):
    d= int(input("Enter the digits for the first set: "))
    a.append(d)
for i in range(h):
    g=int(input("Enter the digits for the second set: "))
    b.append(g)
a=set(a)
b=set(b)

print("Enter what you want to do in the following: \n"
      "1. Union \n"
      "2. intersection \n"
      "3. Difference \n")
z=int(input(""))
if z==1:
    print("a and b is: ",a | b)
elif z==2:
    print("a or b is: ",a & b)
elif z==3:
    print("a minus b is: ",a-b)
else:
    print("Enter a valid input!!")