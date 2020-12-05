data = [i.strip() for i in open('advent2.txt', 'r').readlines()]
print(data)

valid = 0

for j in data:
    n = j.split(' ')
    n[0] = [int(i) - 1 for i in n[0].split('-')]
    n[1] = n[1][0:-1]
    print(n[1])

    #if (n[2][n[0][0]] == n[1]) ^ (n[2][n[0][1]] == n[1]):
    if (n[2][n[0][0]])
        print(n)
        valid += 1



print(valid)
