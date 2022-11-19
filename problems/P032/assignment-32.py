answer=input("would you like to run this code with sample input(y/n)?")
if answer=="y":
    passage="""It was the best of times, it was the worst of times,\n
     it was the age of wisdom, it was the age of foolishness, it was the epoch of belief,\n 
     it was the epoch of incredulity, it was the season of Light,\n
     it was the season of Darkness, it was the spring of hope,\n
      it was the winter of despair."""
else:      
   print("Enter a passage (the passage is finished with END plus it can be multiline passage):")
   i=1
   passage=""
   while (1):
     x=input()
     if x=="END":
        break
     else:    
        passage+=x+"\n"    
print(passage)
x=passage.split()
words=[]
times=[]
k=0
for i in x:
    if (i in words)==False:
        for j in x:
           if i==j:
              k+=1
        words.append(i)
        times.append(k)
    k=0
times_h1=[]
times_h2=[]
for i in words:
    k=0
    m=0
    for j in range(len(x)//2):
        if i==x[j]:
            k+=1
    for t in range(len(x)//2,len(x)):
        if i==x[t]:
            m+=1
    times_h1.append(k)
    times_h2.append(m)
print("\n")           
print("Words used in the passage and their repetition in all passage and first half and second half:")
m=len(words[0])
for i in words:
    if len(i)>m:
        m=len(i)        
for i in range(len(words)):    
    print(" ",words[i],end=" ")
    for j in range(m-len(words[i])):
        print(" ",end="")
    print("{:3d}{:3d}{:3d}".format(times[i],times_h1[i],times_h2[i]),end="")
    if (i+1)%4==0:
        print()
print("\n")           
r=[]
for i in range(len(words)):
    if times_h2[i]>times_h1[i]:
        r.append(words[i])
print("words that are repeated more times in the second half of the passage:")
for i in range(len(r)):
    print(r[i],end="    ")
print("\n")    
letters=[]
times_l=[]
k=0 
for i in passage:       
    if (i in letters)==False:
        for j in passage:
            if i==j:
                k+=1
        letters.append(i)
        times_l.append(k)
    k=0         
print("All characters in the passage and their repetitions:")
for i in range(len(letters)):
    if(letters[i]!="\n"):
        print(letters[i],":{}".format(times_l[i]),end="      ")
    else:
         print("Enter:{}".format(times_l[i]),end="      ")   
    if (i+1)%8==0:
        print("\n")
print("\n")        
w=[]
print("words that thier next word length is more than previous one:")
m=0
for i in range(1,len(x)-1):
    if len(x[i-1])<len(x[i+1]):
        w.append(x[i])
        print("[",x[i-1],w[-1],x[i+1],"]",end="   ") 
        m+=1
    if m==5:
        m=0
        print()
print("\n")               
w1=[]
couple=[]
m=0
for i in range(len(x)-1):
    if x[i][len(x[i])-1]==x[i+1][0]:
      couple.append(x[i])
      couple.append(x[i+1])
      w1.append(couple[m:m+2])
      m+=2        
print("words that their end character is beginning character of next word:")
for i in w1:
    print(i)
