import copy

accumulator = 0


instructions = [(i.strip().split(' ')) for i in open('advent8.txt', 'r').readlines()]

#print(instructions)

i = 0

# part 1
'''
while True:
    line = instructions[i]
    
    print(line)

    if (line, i) in used_instructions:
        break

    used_instructions.append((line, i))

    t = line[0]
    n = line[1]

    if '-' in n:
        n = int(n)
    elif '+' in n:
        n = int(n[1:])

    if t == 'acc':
        accumulator += n
        i += 1
    elif t == 'jmp':
        i += n
    else:
        i += 1
    print(n, i)
'''
#print(accumulator)

prev_j = 0

ts = ['nop', 'jmp']

def prog(instructions):
    accum = 0
    i = 0
    used_instructions = []
    while True:
        
        if i in used_instructions:
            return None
        if i >= len(instructions) - 1:
            return accum
        used_instructions.append(i)
        line = instructions[i]
        t = line[0]
        n = line[1]
        if '-' in n:
            n = int(n)
        elif '+' in n:
            n = int(n[1:])
        if t == 'acc':
            accum += n
        elif t == 'jmp':
            i += n
            continue

        i += 1

new_instructions = instructions.copy()

for j in range(len(instructions)):
    t = instructions[j][0]

    if t == 'jmp':
        new_instructions[j][0] = 'nop'
    elif t == 'nop':
        new_instructions[j][0] = 'jmp'

    succ = prog(new_instructions)

    if succ:
        print(succ)
    else:
        new_instructions = instructions.copy()

print(new_instructions)