import turtle
import random
import time


screen = turtle.Screen()
screen.title("Rabbit vs Tortoise - The River Side Race")
screen.setup(width=1000, height=700)
screen.bgcolor("skyblue") 
screen.tracer(0) 

artist = turtle.Turtle()
artist.hideturtle()


def draw_rectangle(color, x, y, width, height):
    artist.penup()
    artist.goto(x, y)
    artist.setheading(0)
    artist.pendown()
    artist.color(color)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(width)
        artist.right(90)
        artist.forward(height)
        artist.right(90)
    artist.end_fill()

def draw_tree(x, y):
    
    draw_rectangle("brown", x, y, 20, 40)
   
    artist.penup()
    artist.goto(x + 10, y + 10)
    artist.color("darkgreen")
    artist.begin_fill()
    artist.circle(25)
    artist.end_fill()

def draw_river():
   
    draw_rectangle("#1E90FF", -500, 350, 1000, 100)
    
    artist.color("white")
    artist.pensize(2)
    for i in range(-500, 500, 50):
        artist.penup()
        artist.goto(i, 300)
        artist.pendown()
        artist.setheading(-45)
        artist.circle(10, 90)
    artist.pensize(1)



draw_rectangle("limegreen", -500, 250, 1000, 600)


draw_river()


draw_rectangle("gray", -500, -50, 1000, 150)

artist.color("white")
for x in range(-500, 500, 60):
    draw_rectangle("white", x, -120, 30, 8)


tree_positions = [(-400, 200), (-200, 230), (0, 210), (200, 240), (400, 220), 
                  (-350, -220), (50, -250), (300, -210)]
for pos in tree_positions:
    draw_tree(pos[0], pos[1])

artist.penup()
artist.goto(350, -50)
artist.color("black")
artist.pendown()
artist.goto(350, -200)
artist.write(" FINISH", font=("Arial", 16, "bold"))



tortoise = turtle.Turtle()
tortoise.shape("turtle")
tortoise.color("darkgreen")
tortoise.penup()
tortoise.goto(-400, -160)
tortoise.shapesize(1.5)

rabbit = turtle.Turtle()
rabbit.shape("turtle")
rabbit.color("white")
rabbit.penup()
rabbit.goto(-400, -100)
rabbit.shapesize(1.5)

screen.update()
time.sleep(1)


is_race_on = True
rabbit_sleeping = False

while is_race_on:
    
    tortoise.forward(random.randint(2, 5))
    
   
    if not rabbit_sleeping:
        rabbit.forward(random.randint(10, 20)) 
        if rabbit.xcor() > 0:
            rabbit_sleeping = True
    else:
       
        if tortoise.xcor() > rabbit.xcor() + 50:
            rabbit_sleeping = False 
    screen.update()
    time.sleep(0.05)
    
   
    if tortoise.xcor() > 350:
        is_race_on = False
        winner_text = "Tortoise Wins! Slow and steady..."
    elif rabbit.xcor() > 350:
        is_race_on = False
        winner_text = "Rabbit Wins!"


artist.penup()
artist.goto(0, 0)
artist.color("darkred")
artist.write(winner_text, align="center", font=("Arial", 28, "bold"))

screen.update()
screen.exitonclick()