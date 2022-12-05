def readInput():
  with open('./data.txt') as reader:
    return reader.read().splitlines()

def splitText(text: str): 
    textCount = len(text)
    part1 = slice(0, textCount//2)
    part2 = slice(textCount//2, textCount)
    return [text[part1], text[part2]]

def getMatchingChar(text1: str, text2: str):
    return list(set(text1)&set(text2))[0]

def getBadgeChar(text1: str, text2: str, text3: str):
    return list(set(text1)&set(text2)&set(text3))[0]

def chunkify(list, size):
    return [list[i:i + size] for i in range(0, len(list), size)]

def getCharPoint(char: str):
    offset = 0
    if (char.islower()):
        offset = 96
    else: 
        offset = 38

    return ord(char)-offset

# Part 1
tot = 0
for row in readInput():
    splittedText = splitText(row)
    char = getMatchingChar(splittedText[0], splittedText[1])
    tot += getCharPoint(char)
print(tot)

# Part 2
chunks = chunkify(readInput(), 3)
tot = 0
for group in chunks:
    bags = []
    for bag in group:
        bags.append(bag)
    badgeChar = getBadgeChar(bags[0], bags[1], bags[2])
    tot += getCharPoint(badgeChar)
print(tot)



