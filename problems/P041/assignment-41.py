answer=input("would you like to run this code with sample input(y/n)?")
if answer=="y":
    numbers=[23,45,1,89,100,2,31,345,67,70,20]
else:
    numbers=input("Enter numbers:").split()
    for i in numbers:
        i=int(i)        
for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]:
            k=numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=k
print(numbers)                    
