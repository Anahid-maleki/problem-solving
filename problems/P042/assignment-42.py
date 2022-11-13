import math
def func(a,b,y,d):
    dim=[]
    o_c=[1,1,1,1]   # o_c[i] is related to k[i] which if it is 1 means (a,b) is open from k[i] if zero means it is blocked
    k=[(a-1,b),(a+1,b),(a,b-1),(a,b+1)]
    m=0
    for i in range(4):
       if k[i] in y:
        o_c[i]=0
        m+=1
       else:
        dim.append(k[i])
    if d==1:    
       return m
    elif d==2:
        return(dim)
def find_path(x,y,n):
    if x[0][0]>x[1][0]:
       max_x=x[0][0]+1
    else:
        max_x=x[1][0]+1
    if x[0][1]>x[1][1]:
       max_y=x[0][1]+1
    else:
        max_y=x[1][1]+1       
    min_x=0
    min_y=0
    for i in range(len(y)):
        if y[i][0]>max_x:
            max_x=y[i][0]
        if y[i][1]>max_y:
            max_y=y[i][1]
    print("max_x=",max_x,"max_y=",max_y) 
    c=[(i,j) for i in range(min_x,max_x+1) for j in range(min_y,max_y+1)] # all dimensions on the play ground  
    for i in range(len(c)):
        if c[i][0]==0 or c[i][0]==10 or c[i][1]==0 or c[i][1]==10 :
            y.append(c[i])
    for i in range(len(c)):
        if c[i][0]==0 or c[i][0]==10 or c[i][1]==0 or c[i][1]==10 or c[i] in y:
            c[i]="( *  )"        
    for i in range(len(c)):
        if c[i]!="( *  )" and c[i]!=x[0]and c[i]!=x[1] and func(c[i][0],c[i][1],y,1)>=3 :
            if c[i] not in y:
                y.append(c[i])
            c[i]="( *  )"
    m=0
    print("display of all dimentions which are not blocked:")             
    for i in range(max_y+1):
        for j in range(m,m+max_x+1):
            print(c[j],end="   ")
        m+=max_x+1
        print()
    (a,b)=x[0]
    m=0
    path=[x[0]]
    p_path=[]
    s=0
    while (a,b)!=x[1]:
        p_path.append(func(a,b,y,2)) 
        if len(p_path[-1])==0:
            p_path.pop()
            while len(p_path[-1])==1 and path[-2]!=x[0]:
                y.append(path[-1])
                path.pop()
                p_path.pop()
            if len(p_path[-1])==1 and path[-2]==x[0] or p_path==[]:      # there isn't any branches so all the path we return and p_path get=[]
               s=1
               break
            else:   
                y.append(path[-1])        
                p_path.pop()
                (a,b)=path[-1]
        elif len(p_path[-1])==1:
            y.append((a,b))
            path.append((p_path[-1][0]))
            (a,b)=p_path[-1][0]
        else:
            m=0
            y.append((a,b))
            min=math.sqrt((p_path[-1][0][0]-x[1][0])**2+(p_path[-1][0][1]-x[1][1])**2)
            for i in range(1,len(p_path[-1])):
                if math.sqrt((p_path[-1][i][0]-x[1][0])**2+(p_path[-1][i][1]-x[1][1])**2)<min:
                    m=i
            path.append(p_path[-1][m])
            (a,b)=path[-1]    
    if s==1:
        print("Case#",n+1)
        print("IMPOSSIBLE")
    else:
        print("Case#",n+1)            
        print("path=",path) 
answer=input("Would you like to run this code with a sample input(y/n)?")
if answer=="y":
    x2=[[(4, 2),(7, 9)],[(4, 2),(7,9)]]
    y2=[[(2, 1),(2,2),(3,2),(3,3),(4,3),(5, 3),(5,2),(6,2),(7,2),(7,4),(7,3),(8,3),(10,2),(10,3),
         (10,4),(10,5),(10,6),(9,6),(8,6),(7,6),(7,7),(6,7),(6,6),(5,6),(3,5),(3,6),(4,6),(4,8),
         (3,8),(3,9),(4,9),(5,9),(5,10)],[(8,3),(7,3),(7,5),(7,4),(6,4),(7,6),(8, 6),(9,6),(10,6),
         (10,5),(10,4),(10,3),(10,2),(6,1),(6,2),(6,3),(5,3),(5,4),(5,5),(4,5),(3,5),(3,4),(3,3),
         (3,2),(2,2),(2,1),(3,1),(4,1),(5,1)]]
    n=2
else:                 
    t=[]
    y1=[]
    x1=[]
    y2=[]
    x2=[]
    z=0
    n=int(input("Enter the numbers of pathes to be looked for:"))
    g=0
    h=0
    for i in range(n):
        k=input("Enter coordinates of start and end:")
        m=int(input("Enter numbers of boundray limits:"))
        for j in range(m):
            s=input("coordinates of boundry limit:")
            k+=s
        i=0    
        while i<len(k):
            if k[i]=="(" or k[i]=="," or k[i]==")":
                t.append(i)
            i+=1        
        for i in range(h,len(t),3):
            a=int(k[t[i]+1:t[i+1]])
            b=int(k[t[i+1]+1:t[i+2]])
            s=(a,b)
            y1.append(s)
        h=len(t)     
        for i in range(2):
            x1.append(y1[g])
            y1.pop(g)     
        y2.append(y1[g:len(y1)]) 
        x2.append(x1[z:z+2])
        z+=2
        g=len(y1)      
for i in range(n):
    find_path(x2[i],y2[i],i)        