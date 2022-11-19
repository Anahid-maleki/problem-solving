answer=input("Would you like to run this code with sample input(y/n)?")
import random 
if answer=="y":
    x=random.randint(3,7)
    t=[]
    for i in range(x):
        m=random.randint(4,10)
        y=list(map(lambda x: random.randint(1, 20),list(range(0,m))))
        t.append(y)
    print("all lists=",t)
else:     
    x=int(input("Enter a number:"))
    t=[]
    for i in range(x):
        y=input("Enter group of numbers:").split()
        s=list(map(lambda x:int(x),y))
        t.append(s)
    print("all lists=",t)     
c=[]       
for i in range(len(t[0])):
    for j in range(len(t[1])):
        if t[0][i]==t[1][j]:
            c.append(t[0][i])
            t[1].pop(j)
            break
print("common numbers between first and second list:",c) 
i=0 
s=0
j=2            
while i<len(c):
    for j in range(2,len(t)):
        if c[i] not in t[j]:
            c.pop(i)
            i-=1
            if c==[]:
                s=1
            break
        else:
            t[j].remove(c[i])
    if s==1:
        break    
    i+=1        
if c==[]:
    print("there isn't any common numbers between lists.")
else:
    print("common numbers between lists is/are:",c)    