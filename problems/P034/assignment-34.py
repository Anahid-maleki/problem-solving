from bitarray import bitarray
import datetime
x=input("Enter a number:")
s=datetime.datetime.now()
n=int(x)
c=""
prime=bitarray(n+1)
prime.setall(True)
prime[0]=False
prime[1]=False
i=2
while i*i<n+1:
    if prime[i]==True:
        for j in range(i*i,n+1,i):
            if prime[j]!=False:
               prime[j]=False
    i+=1
numbers=[]                        
for i in range(len(x)):
    for j in range(i,len(x)):
        c+=x[j]
        numbers.append(int(c))
    c=""
for i in range(len(numbers)):
        if prime[numbers[i]]==True:
            print(numbers[i])            
a=datetime.datetime.now() 
c=a-s
print("time: ",int(c.total_seconds()) ) 