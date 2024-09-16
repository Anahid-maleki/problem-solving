import math
answer=input("Do you like to run this code with sample input (y/n)?")
if answer=="y":
  w=1000
  h=1000
  x=5
  stars=[["Luna",500,230],
         ["Virgo",260,450],
         ["Altair",120,890],
         ["Miram",530,20],
         ["Cyg",1000,650]]
  p=[200,300]
  target="Altair"
else:    
  w,h=input("Enter dimensions of your world(width and height):").split()
  w=int(w)
  h=int(h)
  x=int(input("Enter numbers of stars in this world:"))
  stars=[]
  for i in range(x):
    m=input("Enter name and coordinates of star number{}:".format(i+1)).split()
    m[1]=int(m[1])
    m[2]=int(m[2])
    stars.append(m)
  p=input("Enter your coordinates in the world:").split()
  p[0]=int(p[0])
  p[1]=int(p[1])
  target=input("Enter your first star name target:")
for i in range(len(stars)):
    if stars[i][0]==target:
        m=i
        distance=math.sqrt((p[0]-stars[i][1])**2+(p[1]-stars[i][2])**2)
        t=distance/0.002   #light travel speed 2*10^-3 AU/s
print("{:.2f}".format(t),target)
p[0]=stars[m][1]
p[1]=stars[m][2]
stars.pop(m)
min=math.sqrt(w**2+h**2)
while(len(stars)):
    min=math.sqrt(w**2+h**2)
    for i in range(len(stars)):
        distance=math.sqrt((p[0]-stars[i][1])**2+(p[1]-stars[i][2])**2)
        if distance<min:
           min=distance
           m=i
    t=min/0.002
    print("{:.2f}".format(t),stars[m][0])
    p[0]=stars[m][1]
    p[1]=stars[m][2]
    stars.pop(m)       



        

