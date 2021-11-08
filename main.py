from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=1000)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
line_y_positions = [-85, -55, -25, 5, 35, 65, 95]
all_turtles = []
all_lines = []


# Create race lines

for line_index in range(0, 7):
    new_line = Turtle()
    new_line.hideturtle()
    new_line.speed("fast")
    new_line.color("black")
    new_line.penup()
    new_line.goto(x=-500, y=line_y_positions[line_index])
    new_line.pendown()
    new_line.forward(1000)
    all_lines.append(new_line)

# Create finish line

finish_line = Turtle()
finish_line.hideturtle()
finish_line.speed("fastest")
finish_line.color("black")
finish_line.penup()
finish_line.goto(x=450, y=line_y_positions[6])
finish_line.pendown()
finish_line.right(90)
finish_line.forward(180)

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-450, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 450:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

