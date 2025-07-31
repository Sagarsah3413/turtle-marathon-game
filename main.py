from turtle import Turtle,Screen
import random
is_race_on = False
colors = ['red','orange','yellow','green','blue','purple']
screen = Screen()
turtles = []
screen.setup(500,400)
# user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter a color: ")
user_bet = screen.textinput(title="Make Your Bet",prompt="Make a Bet, Enter a color: 'red','orange','yellow','green','blue','purple' ")

print(f"Player Bet : {user_bet}")
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-215, y=-70 + i * 35)
    turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have Lost! The {winning_color} turtle is the winner!")

        distance = random.randint(1,10)
        turtle.forward(distance)


screen.exitonclick()