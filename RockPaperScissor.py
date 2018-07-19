#!/bin/python3
from random import randint
#Rock, paper and scissor game

print('Welcome to rock, paper and scissor game!!!')
player = input('rock(r), paper(p), or scissor(s)?')
print(player, 'vs', end=' ')

#getting random number for computer
chosen = randint(1,3)

#assigning rock, paper and scissor by number
if chosen == 1:
  computer = 'r'
elif chosen == 2:
  computer = 'p'
else:
  computer = 's'
print(computer)

if player == computer:
  print('DRAW!')
elif player == 'r' and computer == 's':
  print('Player wins!')
elif player == 'r' and computer == 'p':
  print('Computer wins!')
elif player == 'p' and computer == 'r':
  print('player wins!')
elif player == 'p' and computer == 's':
  print('computer wins!')
elif player == 's' and computer == 'r':
  print('computer wins!')
elif player == 's' and computer == 'p':
  print('player wins!')
