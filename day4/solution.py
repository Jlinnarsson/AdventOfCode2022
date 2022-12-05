def readInput():
  with open('./data.txt') as reader:
    return reader.read().splitlines()

def isPairFullyOverlapping(first: str, second: str):
    firstVaules = first.split('-')
    secondVaules = second.split('-')
    if ((int(firstVaules[0]) <= int(secondVaules[0]) and int(secondVaules[1]) <= int(firstVaules[1])) 
        or 
        (int(secondVaules[0]) <= int(firstVaules[0]) and int(firstVaules[1]) <= int(secondVaules[1]))):
        return True

def isPairOverlapping(first: str, second: str):
    firstVaules = first.split('-')
    secondVaules = second.split('-')
    if (int(firstVaules[1]) > int(secondVaules[0]) or int(secondVaules[1]) > int(firstVaules[0])):
        return True

fullyOverlappingPairs = 0
overlappingPairs = 0
for row in readInput(): 
    pairs = row.split(',')
    if isPairFullyOverlapping(pairs[0], pairs[1]):
        fullyOverlappingPairs += 1 
        
    if (isPairOverlapping(pairs[0], pairs[1])):
        overlappingPairs += 1

print(fullyOverlappingPairs)        
print(overlappingPairs)


