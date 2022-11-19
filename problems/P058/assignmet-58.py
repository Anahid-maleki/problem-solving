def levenshtein(x,y,m):
    a=[]
    a.append(list(range(len(x)+1)))
    for i in range(1,len(y)+1):
        a.append([i]+list(map(lambda i:0 ,list(range(len(x))))))   
    for i in range(1,len(y)+1):
        for j in range(1,len(x)+1):
            if x[j-1]!=y[i-1]:
                min=a[i-1][j-1]
                if a[i][j-1]<min:
                    min=a[i][j-1]
                if a[i-1][j]<min:
                    min=a[i-1][j]
                a[i][j]=min+1
            else:
                a[i][j]=a[i-1][j-1]
    print("levenshtien distance of case number",m+1,"which are",x," and ",y,"is:",a[i][j])
answer=input("would you like to run this code with sample inputs(y/n)?")
if answer=="y":
    n=3
    a=["abcdefg","Like","Human"]
    b=["cdefgh","Bike","Humor"]
    for i in range(len(a)):
        levenshtein(a[i],b[i],i) 
else:
    n=int(input("Enter the number of cases:"))
    a=[]
    b=[]
    for i in range(n):
        x=input("Enter first string:")
        y=input("Enter second string:")
        a.append(x)
        b.append(y)
    for i in range(len(a)):
        levenshtein(a[i],b[i],i)    