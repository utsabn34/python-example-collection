#!/bin/python3

import pygal

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
map = {}
file = open('pets.txt', 'r')

#adding file content in a map
for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    map[label] =value    
file.close()


piechart2 = pygal.Pie()
barchart = pygal.Bar()
linechart = pygal.Line()

#populating data in different chart
for label in map:
  piechart2.add(label, int(map.get(label)))
  barchart.add(label, int(map.get(label)))
  linechart.add(label, int(map.get(label)))
  
  
#displaying chart
piechart2.render()
barchart.render()
linechart.render()


