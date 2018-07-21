#!/bin/python3

import pygal

piechart = pygal.Pie()
#barchart = pygal.Bar()
piechart.title = 'Favourite Animal'
piechart.add('Dog', 6)
piechart.add('Cat',5)
piechart.add('Cow', 7)
piechart.add('Snake', 2)
piechart.add('Hamster', 3)
piechart.render()


barchart = pygal.Bar()
barchart.title = 'Favourite Animal'
barchart.add('Dog', 6)
barchart.add('Cat',5)
barchart.add('Cow', 7)
barchart.add('Snake', 2)
barchart.add('Hamster', 3)
barchart.render()

