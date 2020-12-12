import time
from copy import deepcopy, copy

seats = [' ' + i.strip() + ' ' for i in open('advent11.txt', 'r')]

f_l = ' ' * len(seats[0])

seats = [f_l] + seats + [f_l]

print(seats)

start = time.time()

def adj(seats, row, col):
    adj_seats = ''

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            adj_seats += seats[r][c]

    return adj_seats

def make_new_row(seats, curr_row):
    for char in curr_row:
        adj_seats = adj(seats, row, col)
        if char == 
    return new_row

def part1(seats):
    curr_seats = deepcopy(seats[:])

    while True:
        change = 0
        new_seats = []



        for row in range(1, len(curr_seats)-1):
            curr_row = ''
            for col in range(1, len(curr_seats[row])-1):

                if adj_seats.count('#') == 0 and curr_seats[row][col] == 'L':
                    curr_row += '#'
                    change += 1
                elif adj_seats.count('#') >= 4 and curr_seats[row][col] == '#':
                    curr_row +='L'
                    change += 1
                else:
                    curr_row += curr_seats[row][col]

            new_seats.append(' ' + curr_row + ' ')  
        
        curr_seats = deepcopy(new_seats[:])

        if change == 0:
            break
            
    #return curr_seats
    return sum([seat.count('#') for seat in seats])

new_seats = part1(seats)

#for seat in new_seats:
#    print(' '.join(seat))

print(part1(seats))

