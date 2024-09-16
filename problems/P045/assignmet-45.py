import turtle as t
def draw(a,b):
  s=t.getscreen()
  s.setup(500,500)
  if a=="rectangle":
    print(a,b[0],b[1])
    for i in range(2):
      t.forward(b[0])
      t.left(90)
      t.forward(b[1])
      t.left(90)
  else:   
    for i in range(dict[a]):
      t.forward(b[0])
      t.left(180-((dict[a]-2)*180/dict[a]))
  s.exitonclick() 
def draw1(radius):
  s=t.getscreen()
  s.setup(500,500)
  t.circle(radius)
  s.exitonclick() 
def draw2(radius):
    s=t.getscreen()
    s.setup(500,500)
    t.left(45)
    t.pensize(2)
    for loop in range(2):
      t.circle(radius[0],90)
      t.circle(radius[1],90)
      s.bgcolor("blue") 
    s.exitonclick()         
dict={"square":4,"triangle":3,"pentagon":5,"rectangle":4}
answer=input("would you like to run this code with sample input(y/n)?")
if answer=="y":
  shape=["oval", "20 100"]
  x=[20,100]
else:  
  shape=input("Enter the name of shape and its dimention:").split(":")
  print(shape)
  c=""
  x=[]
  for i in range(len(shape[1])):
     if shape[1][i].isdigit()==True:
        c+=shape[1][i]
     else:
        x.append(int(c))
        c=""
  x.append(int(c))
  print(x)
if shape[0]=="square" or shape[0]=="triangle" or shape[0]=="pentagon" or shape[0]=="rectangle":          
  draw(shape[0],x)
elif shape[0]=="circle":
    draw1(x[0]) 
elif shape[0]=="oval":
    draw2(x)      
 
   






