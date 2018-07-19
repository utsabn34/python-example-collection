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

#creating turtle1
ada =Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

#creating turtle 2
bob =Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

#creating turtle3
charles =Turtle()
charles.color('yellow')
charles.shape('turtle')
charles.penup()
charles.goto(-160,40)
charles.pendown()

#creating turtle3
goblin =Turtle()
goblin.color('green')
goblin.shape('turtle')
goblin.penup()
goblin.goto(-160,10)
goblin.pendown()

#racing four turtles on a track with random numbers
for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  charles.forward(randint(1,5))
  goblin.forward(randint(1,5))

