instructions = [i.strip() for i in open('advent12.txt', 'r').readlines()]

all_dirs = ['N', 'E', 'S', 'W']

#   N
# W   E
#   S

curr_dir = 'E'

NS = 0
WE = 0

for line in instructions:
    mag = int(line[1:])
    d = line[0]

    if d == 'F':
        if curr_dir == 'E':
            WE += mag
        elif curr_dir == 'W':
            WE -= mag
        elif curr_dir == 'N':
            NS += mag
        elif curr_dir == 'S':
            NS -= mag
    elif d == 'N':
        NS += mag
    elif d == 'S':
        NS -= mag
    elif d == 'E':
        WE += mag
    elif d == 'W':
        WE -= mag
    elif d == 'R':
        curr_dir = all_dirs[(all_dirs.index(curr_dir) + mag // 90) % 4]
    elif d == 'L':
        curr_dir = all_dirs[(all_dirs.index(curr_dir) - mag // 90) % 4]

x,y = 0, 0

sx, sy = 10, 1

for line in instructions:
    d = line[0]
    mag = int(line[1:])

    if d == 'F':
        x += sx * mag
        y += sy * mag
    elif d == 'N':
        sy += mag
    elif d == 'S':
        sy -= mag
    elif d == 'E':
        sx += mag
    elif d == 'W':
        sx -= mag
    elif d == 'L':
        while mag:
            sx, sy = -sy, sx
            mag -= 90
    elif d == 'R':
        while mag:
            sx, sy = sy, -sx
            mag -= 90
    
print(x, y)

print(abs(x) + abs(y))