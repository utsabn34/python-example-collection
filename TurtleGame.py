#!/bin/python3
from turtle import *
from random import randint
#adding a speed to the process
speed(10)
penup()
goto(-140,140)
#creating a track for a race
for step in range(15):
  write(step, align ="center")
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

