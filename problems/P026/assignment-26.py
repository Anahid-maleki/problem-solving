def cal(stack):
    i=-1
    t=0
    print(stack)
    while i >-len(stack):
      if stack[i]=="*":
        stack[i+1]*=stack[i-1]
        t=1
      elif stack[i]=="/":
        stack[i+1]/=stack[i-1]
        t=1
      elif stack[i]=="%":
        stack[i+1]%=stack[i-1]
        t=1
      if t:
        stack.pop(i)
        stack.pop(i)
        print(stack)
        i+=1
        t=0            
      i-=1
    print(stack)
    i=-1
    t=0
    while  i >-len(stack): 
      if stack[i]=="+":
        stack[i+1]+=stack[i-1]
        t=1
      elif stack[i]=="-":
        stack[i+1]-=stack[i-1]
        t=1
      if t:
        stack.pop(i)
        stack.pop(i)
        t=0
        i+=1  
      i-=1    
    m=stack
    return m

answer=input("do you want to try with sample input?(y/n):")
if answer=="y":
  exp="3+(4+(5-2)*3)+7+(9-2*(7+(6-3)-2)+9)"
else:
  exp=input("Enter a numerical expresion:")
c=""
n=[]
j=0
for i in exp:
    print(i)
    if i.isdigit():
        c+=i
    else:
        if c:
          n.append(int(c))
          n.append(i)
          c=""
        else:
            n.append(i)  
if c:
  n.append(int(c))      
print(n)
i=0
t=0
stack=[]
while i<len(n) :   
  if n[i]=="(":
    open=i
  elif n[i]==")":
    close=i
    t=1
    for i in range(close-1,open,-1):
        stack.append(n[i])    
    n[open:close+1]=cal(stack)
    stack.clear()
    t==0
    open=-1 
    i=-1
    print(n)     
  i+=1 
for i in range(-1,-len(n)-1,-1):
    stack.append(n[i])
n=cal(stack)    
print(exp,"=",n[0])                  