#!/bin/python3

from turtle import *
from random import *

def randomcolor():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    color(red, blue, green)

def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()

def randomheading():
    position = randint(1,360)
    setheading(position)
    
def drawrectangle():
    randomcolor()
    randomplace()
    hideturtle()
    length = randint(1, 100)
    height = randint(10, 100)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()

def drawcircle():
    radius = randint(50, 125)
    randomcolor()
    randomplace()
    begin_fill()
    circle(radius)
    end_fill()

def drawstar():
  radius = randint(50, 125)
  randomcolor()
  randomplace()
  begin_fill()
  for side in range(5):
    left(144)
    forward(50)
  end_fill()

shape("turtle")
speed(0)

#for i in range(3):
#  randomcolor()
#  randomplace()
#  randomheading()
  
clear()
setheading(0)

#for i in range(20):
#    drawrectangle()

# for i in range(40):
#    drawcircle()

for i in range(10):
    drawstar()