import numpy as np

grid = [[0,9,0,3,0,0,0,7,0],
        [0,5,3,4,0,9,0,0,0],
        [0,0,2,0,0,0,0,5,0],
        [0,0,0,2,0,0,0,0,0],
        [2,0,0,1,0,0,6,4,0],
        [0,0,4,5,0,0,0,1,2],
        [0,3,6,0,0,0,4,0,5],
        [0,0,0,9,0,0,0,0,0],
        [1,0,0,0,0,8,0,0,0]]

print("Entered Grid:")
print(np.matrix(grid))

def possible(y,x,n):
    global grid 
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

#test conditions
# print("Is the middle square 3? " + str(possible(4,4,3)))
# print("Is the middle square 5? " + str(possible(4,4,5)))

# print(0//3*3)
# print(1//3*3)
# print(2//3*3)
# print(3//3*3)
# print(4//3*3)
# print(5//3*3)
# print(6//3*3)
# print(7//3*3)
# print(8//3*3)

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return 
    print(np.matrix(grid))


print("Solution")
solve()