field = [i.strip() for i in open('advent3.txt', 'r').readlines()]

row = 0
column = 0
trees = 0


while row < len(field):
    column = column % 31

    if field[row][column] == '#':
        trees += 1

    row += 1
    column += 1

print(trees)

row = 0
column = 0
trees = 0


while row < len(field):
    column = column % 31

    if field[row][column] == '#':
        trees += 1

    row += 1
    column += 3

print(trees)

row = 0
column = 0
trees = 0

while row < len(field):
    column = column % 31

    if field[row][column] == '#':
        trees += 1

    row += 1
    column += 5

print(trees)

row = 0
column = 0
trees = 0


while row < len(field):
    column = column % 31

    if field[row][column] == '#':
        trees += 1

    row += 1
    column += 7

print(trees)

row = 0
column = 0
trees = 0

while row < len(field):
    column = column % 31
    
    if field[row][column] == '#':
        trees += 1

    row += 2
    column += 1

print(trees)

print(75*294*79*85*39)
