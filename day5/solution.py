def readInput():
  with open('./data.txt') as reader:
    return reader.read()

def chunkify(list, size):
    return [list[i:i + size] for i in range(0, len(list), size)]

def createDataStructure(input: str):
    data = [[], [], [], [], [], [], [], [], []]
    chunks: list[str] = []
    for row in input.splitlines()[:-1]:
        chunks.append(chunkify(row, 4))
        
    for chunk in chunks:
        for i, value in enumerate(chunk):
            if (value == '    ' or value == '   '):
                continue
            data[i].append(value.rstrip().lstrip())

    for row in data: 
        row.reverse()
    return data

def processInstruction(*data: list[list], instruction: str):
    instructionParts = instruction.split()
    print(instructionParts[1], instructionParts[3], instructionParts[5])
        
input = readInput()
containers, instructions = input.split('\n\n')
table = createDataStructure(containers)

for instruction in instructions.splitlines():
    instructionParts = instruction.split()

    amount = int(instructionParts[1])
    takeFrom = int(instructionParts[3])-1
    moveTo = int(instructionParts[5])-1

    moving = table[takeFrom][-amount:]
    table[takeFrom] = table[takeFrom][:-amount]
    moving.reverse() #Remove this for part2, yes lazy solution and might clean. 
    table[moveTo].extend(moving)

text = ""
for row in table:
    text += row[len(row)-1]
print(text)
