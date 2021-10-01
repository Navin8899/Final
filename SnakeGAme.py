import turtle
import time
import random


                          #"""  Variable Decleration  """
delay=0.1
score = 0
heighestscore = 0
bodies=[]
                         #"""  Screen   """
s= turtle.Screen()
s.title("Snake Game Created By Naveen Kumar")
s.bgcolor("gray")
s.setup(width=700,height=600)

                         #"""   Head Turtle   """
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.penup()
head.goto(0,0)
head.color("white")
head.fillcolor("blue")
head.direction="stop"


                   #"""   Food Turtle  """
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.fillcolor("lime")
food.penup()
food.ht()
food.goto(0,140)
food.st()

                   #"""   Score board    """
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-335,-285)
sb.write("Your Score:0 ")


           #"""   Function for movement """
def moveup():
    if head.direction!="down":
        head.direction='up'
        
def movedown():
    if head.direction!="up":
        head.direction='down'

def moveleft():
    if head.direction!="right":
        head.direction='left'

def moveright():
    if head.direction!="left": 
        head.direction='right'

def movestop():
    head.direction="stop"
    
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)    

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        

          #"""     Key Event   """        
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")


             #"""   Round Screen   """
while True:
    s.update()
    if head.xcor()>320:
        head.setx(-320)
        
    if head.xcor()<-320:
        head.setx(320)
        
    if head.ycor()>295:
        head.sety(-295)
        
    if head.ycor()<-295:
        head.sety(295)    

    """   FOOD   """    
    if head.distance(food)<20:
       
        x=random.randint(-320,320)
        y=random.randint(-280,280)
        food.goto(x,y)
     

        #lenght increase
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color('red')
        body.fillcolor("black")
        bodies.append(body)
        
        score+=10
        
        delay=delay-0.001

        if score>heighestscore:
            heighestscore=score
        sb.clear()
        sb.write("Your Score: {}".format(score,heighestscore)) 


#"""  MOVE THE TURTLE OF BODY  """    
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
        
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()    
        bodies[0].goto(x,y)
    move()    


#"""   TOUCH FROM OWN BODY   """
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for body in bodies:
                body.ht()
            bodies.clear()
            
            score=0
            delay=0.1

            sb.clear()
            sb.write("score: {}".format(score)) 
    time.sleep(delay)    
s.mainloop()    
    


        































    
        






























     





















        
