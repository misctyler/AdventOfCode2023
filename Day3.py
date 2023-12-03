import math as m, re

file_path = 'Day 3 Input.txt'
matrix = list(open(file_path))
dubstep = range(140) #ayy lmao

chars = {(row, column): [] for row in dubstep for column in dubstep
         if matrix[row][column] not in '01234566789.'}

for r in range(len(matrix)):
    for n in re.finditer(r'\d+', matrix[r]):
        edge = {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}
        for x in edge & chars.keys():chars[x].append(int(n.group()))

print("Sum of Part Numbers: " + str(sum(sum(x)    for x in chars.values())))
print("Sum of Gear Ratios:  " + str(sum(m.prod(x) for x in chars.values() if len(x)==2)))
