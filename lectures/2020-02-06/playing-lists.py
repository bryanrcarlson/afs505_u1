# create list

a = [[10, 11, 12], [20, 21, 22], [30, 31, 32]]
print(a[0], a[1], a[2], sep = "\n")

# [10, 11, 12]
# [20, 21, 22]
# [30, 31, 32]

# so: a[row][col]

# printing
for row in range(len(a)):
    for col in range(len(a[row])):
        print(a[row][col], end = ' ')
    print()

# dynamic creations
n = 3
m = 4
a = [0] * n # takes list and duplicates n times
for i in range(n):
    a[i] = [0] * m

# or
n = 3
m = 4
a2 = []
for i in range(n):
    a2.append([0] * m)

# or

rowCount = 3
colCount = 4
board = []
for row in range(rowCount):
    currRow = []
    for col in range(colCount):
        currRow.append(0)
    board.append(currRow)
print(board)