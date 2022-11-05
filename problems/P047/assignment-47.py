from bitarray import bitarray
import datetime
x=int(input("Enter a number:"))
s=datetime.datetime.now()
prime=bitarray(x+1)
prime.setall(True)
i=3
while i*i<x+1:
    if prime[i]==True:
        for j in range(i*i,x+1,2*i):
            prime[j]=False
    i+=2        
k=1 #cause 2 is the only even prime number
for i in range(3,x+1,2):
    if prime[i]==True:
        k+=1
print(k)
a=datetime.datetime.now() 
c=a-s
print("time: ",int(c.total_seconds()) )                    