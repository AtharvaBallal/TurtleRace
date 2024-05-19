import random
from turtle import Turtle, Screen

colors = ["red", "orange", "pink", "green", "blue", "purple"]
x = -430
y = -100
is_race_on = False
turtles = []

screen = Screen()
screen.setup(900, 900)

user_input = screen.textinput("Bet",
                              "Choose the turtle color from below to bet:\nRed, Orange, Pink, Green, Blue, Purple,").lower()

for i in range(6):
    tuktuk = Turtle(shape="turtle")
    tuktuk.penup()
    tuktuk.color(colors[i])
    tuktuk.goto(x, y)
    y += 50
    turtles.append(tuktuk)

if user_input:
    is_race_on = True

while is_race_on:
    for tuk in turtles:
        if tuk.xcor() >430:
            is_race_on = False
            winning_color = tuk.pencolor()
            if winning_color == user_input:
                print(f"You Have Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You Have Lost! The {winning_color} turtle is the winner.")
        rand_dist = random.randint(0, 10)
        tuk.forward(rand_dist)


screen.exitonclick()
