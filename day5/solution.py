def readInput():
  with open('./data.txt') as reader:
    return reader.read().splitlines()

def chunkify(list, size):
    return [list[i:i + size] for i in range(0, len(list), size)]

def createDataStructure():
    data = []
    chunks: list[str] = []
    for row in readInput():
        chunks.append(chunkify(row, 4))
        
    for chunk in chunks:
        for i, value in enumerate(chunk):
            if (value == '    ' or value == '   ') or v:
                continue
            print(value.rstrip().lstrip(), i)
        





createDataStructure()

