from turtle import Turtle, Screen
import random

#
# class TurtleList:
#
#     def __init__(self,name, color):
#         self.name = name
#         self.color = color

screen = Screen()
screen.setup(width=500, height=400)
print("Turtle: blue, red, green, pink, orange, purple")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

game_continue = True
turtle_speed = [1, 2, 3, 4, 5]
# turtle_list = [{"name": "t1","color":"blue"},
#                {"name": "t2","color":"red"},
#                {"name": "t3","color":"green"},
#                {"name": "t4","color":"pink"},
#                {"name": "t5","color":"orange"},
#                {"name": "t6","color":"purple"}]
#
#
# turtle_id = []
# for i in turtle_list:
#     turtle_name = turtle_list["name"]
#     turtle_color = turtle_list["color"]
#     turtle_idenity = TurtleList(turtle_name,turtle_color)
#     turtle_id.append(turtle_idenity)
#     print(turtle_id.name)
#
#







jim = Turtle(shape='turtle')
jim.color("red")

terry = Turtle()
terry.shape("turtle")
terry.color("blue")

jerry = Turtle()
jerry.shape("turtle")
jerry.color("green")

tommy = Turtle()
tommy.shape("turtle")
tommy.color("orange")

garry = Turtle()
garry.shape("turtle")
garry.color("black")

randy = Turtle()
randy.shape("turtle")
randy.color("pink")

jim.penup()
jim.goto(x=-230, y=150)
terry.penup()
terry.goto(x=-230, y=100)
jerry.penup()
jerry.goto(x=-230, y=50)
tommy.penup()
tommy.goto(x=-230, y=0)
garry.penup()
garry.goto(x=-230, y=-50)
randy.penup()
randy.goto(x=-230, y=-100)

# print(jim.pos())
# print(jerry.pos())

jim_progress = 0
terry_progress = 0
jerry_progress = 0
tommy_progress = 0
garry_progress = 0
randy_progress = 0

while game_continue:
    jim_speed = random.choice(turtle_speed)
    jim.forward(jim_speed)
    jim_progress += jim_speed

    terry_speed = random.choice(turtle_speed)
    terry.forward(terry_speed)
    terry_progress += terry_speed

    jerry_speed = random.choice(turtle_speed)
    jerry.forward(jerry_speed)
    jerry_progress += jerry_speed

    tommy_speed = random.choice(turtle_speed)
    tommy.forward(tommy_speed)
    tommy_progress += tommy_speed

    garry_speed = random.choice(turtle_speed)
    garry.forward(garry_speed)
    garry_progress += garry_speed

    randy_speed = random.choice(turtle_speed)
    randy.forward(randy_speed)
    randy_progress += randy_speed

    if jim_progress > 500:
        game_continue = False
        winner = "red"
    elif terry_progress > 500:
        game_continue = False
        winner = "blue"
    elif jerry_progress > 500:
        game_continue = False
        winner = "green"
    elif tommy_progress > 500:
        game_continue = False
        winner = "orange"
    elif garry_progress > 500:
        game_continue = False
        winner = "black"
    elif randy_progress > 500:
        game_continue = False
        winner = "pink"

# print(jim_progress)
# print(terry_progress)
# print(jerry_progress)
# print(tommy_progress)
# print(garry_progress)
# print(randy_progress)
# print(winner)

if user_bet.lower() == winner.lower():
    print(f"You win! the winner is {winner}.")
else:
    print(f"You lose! the winner is {winner}.")

screen.exitonclick()
