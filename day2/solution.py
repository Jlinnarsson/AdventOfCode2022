def ReadInput():
  with open('./data.txt') as reader:
    return reader.read().splitlines()

pointsPart1 = 0
pointsPart2 = 0 
for row in ReadInput():
  x, y = row.split()

  #Part 1
  shapePoints = {'X': 1, 'Y': 2, 'Z': 3}
  pointsPart1 += shapePoints[y]
  gamePoints = {
    ('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'): 3,
    ('A', 'Y'): 6, ('A', 'Z'): 0,
    ('B', 'X'): 0, ('B', 'Z'): 6,
    ('C', 'X'): 6, ('C', 'Y'): 0
  }
  pointsPart1 += gamePoints[(x, y)]

  #Part 2 
  shapePointsPart2 = {'X': 0, 'Y': 3, 'Z': 6}
  pointsPart2 += shapePointsPart2[y]
  gamePointsPart2 = {
    ('A', 'X'): 3, ('B', 'Y'): 2, ('C', 'Z'): 1,
    ('A', 'Y'): 1, ('A', 'Z'): 2,
    ('B', 'X'): 1, ('B', 'Z'): 3,
    ('C', 'X'): 2, ('C', 'Y'): 3
  }
  pointsPart2 += gamePointsPart2[(x, y)]
  
print(pointsPart1)
print(pointsPart2)


