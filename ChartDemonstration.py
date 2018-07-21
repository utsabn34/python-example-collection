#!/bin/python3

import pygal

#rendering data from file
#piechart
file = open('pets.txt', 'r')
piechart2 = pygal.Pie()
for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))
file.close()
piechart2.render()


#rendering static data
#piechart
piechart = pygal.Pie()
piechart.title = 'Favourite Animal'
piechart.add('Dog', 6)
piechart.add('Cat',5)
piechart.add('Cow', 7)
piechart.add('Snake', 2)
piechart.add('Hamster', 3)
piechart.render()


#rendering data from file
#barchart
file = open('pets.txt', 'r')
barchart2 = pygal.Bar()
for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    barchart2.add(label, int(value))
file.close()
barchart2.render()

#rendering static data
#barchart
barchart = pygal.Bar()
barchart.title = 'Favourite Animal'
barchart.add('Dog', 6)
barchart.add('Cat',5)
barchart.add('Cow', 7)
barchart.add('Snake', 2)
barchart.add('Hamster', 3)
barchart.render()

