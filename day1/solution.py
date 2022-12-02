def ReadInput():
  with open('./data.txt') as reader:
    return reader.read().splitlines()

sums = []
tot = 0
for row in ReadInput():
  if row == '':
    sums.append(tot)
    tot = 0
    continue
  tot += int(row)

print(max(sums)) # Step 1 
sums.sort()
print(sum(sums[-3:])) # Step 2