import turtle
import time

#drawing a simple square with parameter some_turtle and distance
def draw_square(some_turtle, distance, fill=False):
    if fill:
        some_turtle.fill(True)
    for i in range (0,4):
        some_turtle.forward(distance)
        some_turtle.right(90)
    if fill:
        some_turtle.fill(False)

#drawing a simple circle with parameter some_turtle and radius
def draw_circle(some_turtle, radius, fill=False):
    if fill:
        some_turtle.fill(True)
    some_turtle.circle(radius)
    if fill:
        some_turtle.fill(False)

#drawing a simple triangle with parameter some_turtle and distance
def draw_triangle(some_turtle, distance, fill=False):
    if fill:
        some_turtle.fill(True)
    for i in range(0, 3):
        time.sleep(2)
        some_turtle.left(120)
        some_turtle.forward(distance)
    if fill:
        some_turtle.fill(False)

def recursive_triangle(some_turtle, min_length):
    for i in range(0,3):
        draw_triangle(some_turtle, min_length, 1)
        some_turtle.penup()
        some_turtle.right(120)
        some_turtle.forward(min_length)
        some_turtle.pendown()

window = turtle.Screen()
window.bgcolor("red")
terry = turtle.Turtle()
terry.color("green")
terry.shape("turtle")
terry.pencolor("blue")
terry.speed(2)
#draw_triangle(terry, 100, 1)
recursive_triangle(terry, 100)
window.exitonclick()