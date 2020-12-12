import time
import logging
from copy import deepcopy, copy

seats = [' ' + i.strip() + ' ' for i in open('advent11.txt', 'r')]

f_l = ' ' * len(seats[0])

seats = [f_l] + seats + [f_l]

#print(seats)

start = time.time()

def part1(seats):
    curr_seats = deepcopy(seats[:])
    
    f_l = seats[0]

    steps = 0

    changing = True

    while changing:
        changing = False

        steps += 1
        new_seats = [f_l]

        for row in range(1, len(curr_seats)-1):
            curr_row = ''
            for col in range(1, len(curr_seats[row])-1):
                adj_seats = ''
                for r in (row-1,row,row+1):
                    for c in (col-1,col,col+1):
                        if r != row or c != col:
                            adj_seats += curr_seats[r][c]

                if adj_seats.count('#') == 0 and curr_seats[row][col] == 'L':
                    curr_row += '#'
                    changing = True
                elif adj_seats.count('#') >= 4 and curr_seats[row][col] == '#':
                    curr_row +='L'
                    changing = True
                else:
                    curr_row += curr_seats[row][col]

            new_seats.append(' ' + curr_row + ' ')  
        
        curr_seats = deepcopy(new_seats[:]) + [f_l]
        
        if not changing:
            break

    return sum([seat.count('#') for seat in new_seats])

print('part 1 available seats:', part1(seats), 'runtime:', time.time() - start, 'seconds.')

def part2(seats):
    changing = True
    steps = 0

    curr_seats = deepcopy(seats[:])

    configs = []

    while changing:
        

        changing = False

        steps += 1
        new_seats = []

        col_seats = {}
        
        for r in range(len(curr_seats)):
            for c in range(len(curr_seats[r])):
                try:
                    col_seats[str(c)] += curr_seats[r][c]
                except:
                    col_seats[str(c)] = curr_seats[r][c]

        for row in range(len(curr_seats)):
            curr_row = ''
            for col in range(len(curr_seats[row])):
                in_sight_seats = curr_seats[row] + col_seats[str(col)]

                if row >= col:
                    new_r = row - col
                    new_c = 0
                elif row < col:
                    new_r = 0
                    new_c = col - row

                while new_r < len(curr_seats) and new_c < len(curr_seats):
                    in_sight_seats += curr_seats[new_r][new_c]
                    new_r += 1
                    new_c += 1

                if row + col < len(curr_seats):
                    new_r = row + col
                    new_c = 0
                elif row + col >= len(curr_seats):
                    new_r = len(curr_seats) - 1
                    new_c = len(curr_seats) - 1 - col

                while new_r > 0 and new_c < len(curr_seats):
                    in_sight_seats += curr_seats[new_r][new_c]
                    new_r -= 1
                    new_c += 1

                if in_sight_seats.count('#') == 0 and curr_seats[row][col] == 'L':
                    curr_row += '#'
                    changing = True
                elif in_sight_seats.count('#') >= 9 and curr_seats[row][col] == '#': # in_sight_seats over counts by 4
                    curr_row +='L'
                    changing = True
                else:
                    curr_row += curr_seats[row][col]

            new_seats.append(curr_row)  
        
        configs.append(new_seats)

        curr_seats = deepcopy(new_seats[:])

        print(steps)

        if not changing:
            break

    return sum([seat.count('#') for seat in new_seats])

start = time.time()

print('part 2 available seats:', part2(seats), 'runtime:', time.time() - start, 'seconds.')

