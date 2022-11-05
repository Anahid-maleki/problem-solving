import math
def find(table,word):
  x=[]
  y=[]
  dimen=[]
  m=0
  n=0
  for i in range(len(word)):
    for j in range(len(table)):
        for k in range(len(table)):
            if table[j][k]==word[i]:
                x.append(j)
                x.append(k)
                y.append(x[m:m+2])
                m+=2
    dimen.append(y[n:len(y)])
    n=len(y)
  m=0 
  a=[]
  b=[]
  s=0
  while m<len(dimen)-1 :   
   for i in range(len(dimen[m])):
       for j in range(len(dimen[m+1])):
           if abs(dimen[m][i][0]-dimen[m+1][j][0])<=1 and abs(dimen[m][i][1]-dimen[m+1][j][1])<=1:
              a.append(dimen[m][i])
              b.append(dimen[m+1][j])
              if m==0:
                s+=1
   z=list(zip(a,b))                     
   m+=1
  p=[]
  q=[]
  k=0
  for i in range(len(b)-1):
    for j in range(i+1,len(a)):
        if b[i]==a[j]:
            p.append(a[i])
            q.append(b[i])
            k=1
            break
    if k==1:
        break
  for j in range(i,len(a)) :
    if a[j]==q[-1]:
        p.append(a[j])
        q.append(b[j]) 
  final=[]
  final.append(p[0])
  for i in range(len(q)):
    final.append(q[i])
  for i in final:
    i[0]+=1
    i[1]+=1
  if len(final)<len(word):
    print(word,"is not found.")  
  else:
    print(word,"=",final)                   
answer=input("would you like to run this with sample input?(y/n):")
if answer=="y":
  x=5
  table=[]
  y=[]
  m=0
  TABLE=[["K","D","E","W","B"],
         ["O","W","A","F","L"],
         ["O","I","T","R","O"],
         ["B","U","R","F","S"],
         ["V","D","T","J","E"]]
  for i in TABLE:
    for j in range(5):
      y.append(i[j].lower())
    table.append(y[m:m+5])
    m+=5     
  word=["sofa","fruit","impossible","dart"]
else:      
  x=int(input("Enter number the dimention of the table:"))
  table=[]
  word=[]
  for i in range (x):
    y=input("Enter letters:")
    table.append((y.lower()).split())
  while(1):
    y=input("Enter words to be searched:")
    if y=="END":
        break
    word.append(y)
print(table)
print(word)
for i in word: 
  find(table,i)