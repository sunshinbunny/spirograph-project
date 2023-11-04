import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
my_screen = Screen()
tim.shape("arrow")
t.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color= r, g, b
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size_of_gap)

draw_spirograph(2)

my_screen.exitonclick()