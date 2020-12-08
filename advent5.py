seats = [(i[0:7], i.strip()[7:]) for i in open('advent5.txt', 'r').readlines()]
row_cols = []
seat_ids = []

def to_row(row_str: str) -> int:
    rows = [i for i in range(128)]
    for d in row_str:
        if d == 'F':
            rows = rows[:len(rows) // 2]
        elif d == 'B':
            rows = rows[len(rows) // 2:]
    return rows[0]

def to_column(col_str: str) -> int:
    cols = [i for i in range(8)]
    for d in col_str:
        if d == 'L':
            cols = cols[:len(cols) // 2]
        elif d == 'R':
            cols = cols[len(cols) // 2:]
    return cols[0]

def get_id(row: int, col: int) -> int:
    return row * 8 + col

for seat in seats:
    row_cols.append((to_row(seat[0]), to_column(seat[1])))

for row, col in row_cols:
    seat_ids.append(get_id(row, col))

print(max(seat_ids)) #part 1

sorted_ids = sorted(seat_ids)

print(sorted_ids)

for i in range(955-71):
    if sorted_ids[i] != i + 71:
        print(i + 71) #part 2
        break

