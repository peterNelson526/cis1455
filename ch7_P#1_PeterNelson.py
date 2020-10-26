"""
Intro to Programming
Author: Peter Nelson
Date: 10/23/2020
Project 1
Function that uses turtle to draw a circle
"""

from turtle import Turtle
import math

def draw_circle(x, y, radius):
    t = Turtle()
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.pencolor("red")
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)    
def main():
    t = Turtle()
    t.speed(10)
    draw_circle(0, 0, 150)

main()
    
