import turtle
import math

length = 600
pf = math.sqrt(3)/2
print(pf)

def draw_triangle(some_turtle, x, y, length):
    some_turtle.penup()
    some_turtle.goto(x, y)
    some_turtle.fill(True)
    some_turtle.pendown()
    some_turtle.forward(length)
    some_turtle.left(120)
    some_turtle.forward(length)
    some_turtle.left(120)
    some_turtle.forward(length)
    some_turtle.penup()
    some_turtle.setheading(0)
    some_turtle.fill(False)
    some_turtle.goto(x,y)

def recursive_triangle(some_turtle, x, y, length, level):
    if (level > 1):
        length = length/2
        recursive_triangle(some_turtle, x, y, length, level-1) #bottom left triangle
        recursive_triangle(some_turtle, x+length, y, length, level-1)
        recursive_triangle(some_turtle, x+length/2, y+length*pf, length, level-1)
    else:
        draw_triangle(some_turtle, x, y, length)

window = turtle.Screen()
window.bgcolor("white")
terry = turtle.Turtle()
terry.color("green")
terry.shape("turtle")
terry.pencolor("blue")
terry.speed(10)
#draw_triangle(terry, 100, 1)
#draw_triangle(terry, -length/2, -length*pf/2, length)
recursive_triangle(terry, -length/2, -length*pf/2, length, 6)

window.exitonclick()