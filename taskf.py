from turtle import Turtle, Screen
import random

scr = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []


for i in range(0, 6):
    t = Turtle()
    t.shape("turtle")
    color = random.choice(colors)
    t.color(color)
    t.penup()
    t.goto(x=-250, y=-i*50 + 100)
    t.pendown()
    
    all_turtles.append(t)
    
scr.setup(width=500, height=400)
scr.title("A corrida das tartarugas")
user_bet = scr.textinput("Aposta!", "Qual tartaruga vai ganhar ??", )

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            print(f"A tartaruga {turtle.pencolor()} ganhou!")
            if user_bet.lower() == turtle.pencolor():
                print("Parabéns, você ganhou a aposta!")
            else: 
                print("Você perdeu a aposta... Aposte novamente!")
           
            
    

scr.exitonclick()