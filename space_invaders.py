#Space Invader 

#setting up the screen
import turtle
import math
import random
import winsound

wn=turtle.Screen()
wn.title("space invaders")
wn.bgcolor("black")
wn.bgpic("aa.gif")




turtle.register_shape("en.gif")


#Drawing the border
'''border=turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pensize(3)
border.pendown()
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()'''

#creating the player
player=turtle.Turtle()
player.color("yellow")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.setposition(0,-250)

#Let's give our player movement
playerspeed=15
enemyspeed=0.5


#Let's create the enemy
enemy=turtle.Turtle()
enemy.color("red")
enemy.shape("en.gif")
enemy.penup()
enemy.speed(0)
x=random.randint(-200,200)
y=random.randint(100,250)
enemy.setposition(x,y)



#Let's create weapon
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#let's create level tag
score = 0
level=turtle.Turtle()
level.speed(0)
level.color("white")
level.penup()
level.setposition(-290,270)
scores="LEVEL: %s" %score
level.write(scores, False, align="left", font=("Arial",14,"normal"))
level.hideturtle()

#let's create gameover tag
gameover=turtle.Turtle()
gameover.speed(0)
gameover.color("white")
gameover.penup()
gameover.setposition(90,100)
yo="GAME-OVER"

gameover.hideturtle()

bulletspeed=20
bulletstate="ready"

def move_right():
    x=player.xcor()
    x=x+playerspeed

    if x>280:
        x = 280
        player.setx(x)
    else:
        player.setx(x)
    

def move_left():
    x=player.xcor()
    x=x-playerspeed
    if x<-280:
        x=-280
        player.setx(x)
    else:
        player.setx(x)

def fire_bullet():
    global bulletstate
    if(bulletstate == "ready"):
        winsound.PlaySound("qw.wav",winsound.SND_ASYNC)
        bulletstate="firing"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def iscollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
    
    

#keyboard binding
turtle.listen()
turtle.onkey(move_right,"Right")
turtle.onkey(move_left,"Left")
turtle.onkey(fire_bullet,"Up")

#main game

while True:
    x=enemy.xcor()
    x=x+enemyspeed
    enemy.setx(x)

    if(enemy.xcor()>280):
        y=enemy.ycor()
        y -=40
        enemyspeed *=-1
        enemy.sety(y)
    if(enemy.xcor()<-280):
        y=enemy.ycor()
        y -=40
        enemyspeed *=-1
        enemy.sety(y)

     #collision checking
    if iscollision(bullet,enemy):
        bullet.hideturtle()
        bulletstate="ready"
        bullet.setposition(0,-400)
        enemy.setposition(-200,250)
        enemyspeed +=2
        score=score+1
        scores="LEVEL: %s" %score
        level.clear()
        level.write(scores,False,align="left", font=("Arial",14,"normal"))
        winsound.PlaySound("ex.wav",winsound.SND_ASYNC)
        

        
    
    z=enemy.ycor()
    if z<-240:
        player.hideturtle()
        enemy.hideturtle()
        gameover.write(yo,False,align="center",font=("Arial",30,"normal"))
        o=input()
    
        break

    #moving the bullet
    if bulletstate=="firing":
        y=bullet.ycor()
        y +=bulletspeed
        bullet.sety(y)
    if(bullet.ycor()>275):
        bullet.hideturtle()
        bulletstate="ready"

   

    


    


    

    

