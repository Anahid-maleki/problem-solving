import math
import datetime
from bitarray import bitarray
x=int(input("Enter primorial number:"))
s=datetime.datetime.now()
prime=bitarray(x+1)
prime.setall(True)
i=3
while i*i<x+1:
    if prime[i]==True:
        prime[i*i:x+1:2*i]=0
    i+=2
m=math.log10(2)   
for i in range(3,x+1,2):
    if prime[i]==True:
        m+=math.log10(i)
print(x,"# =",int(m+1))        
a=datetime.datetime.now() 
c=a-s
print("time: ",int(c.total_seconds()) )          