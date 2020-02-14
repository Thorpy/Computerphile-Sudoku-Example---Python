import numpy as np
import random as rn

#gridexample = [5,3,0,0,7,0,0,0,0,6,0,0,1,9,5,0,0,0,0,9,8,0,0,0,0,6,0,8,0,0,0,6,0,0,0,3,4,0,0,8,0,3,0,0,1,7,0,0,0,2,0,0,0,6,0,6,0,0,0,0,2,8,0,0,0,0,4,1,9,0,0,5,0,0,0,0,8,0,0,7,9]

aArray = []
grid = []
emptygrid = []
solvedgrid = []

def generate() :
    global aArray
    aArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,0,0,3,0,0,4,0,5,0,0,0,6,0,0,7,0,0,8,0,9,0,0,0,0]
    global grid
    rn.shuffle(aArray)
    aArray = np.array(aArray).reshape(9,9)
    grid = aArray

def possible(y,x,n) :
    global grid
    for i in range(0,9) :
        if grid[y][i] == n :
            return False
    for i in range(0,9) :
        if grid[i][x] == n :
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3) :
        for j in range(0,3) :
            if grid[y0+i][x0+j] == n :
                return False
    return True

def solve() :
    global grid
    global solvedgrid
    global emptygrid
    for y in range(9) :
        for x in range(9) :
            if grid[y][x] == 0 :
                for n in range(1,10) :
                    if possible(y,x,n) :
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    solvedgrid = (np.matrix(grid))
    try:
        emptygrid = grid
        with np.nditer(emptygrid, op_flags=['readwrite']) as it:
            for cell in it:
                zeros = rn.randint(0,1)
                if zeros == 0:
                    cell[...] = 0
        print("\n \n")
        print("Here is the generated sudoku")
        print(emptygrid)
        print("\n \n")
        print("Here is the solved sudoku")
        print(np.matrix(solvedgrid))
        print("\n \n")
        input("Generate another?")
    except:
        pass

try:
    generate()
    solve()
except:
    print("\n \nBye then!")
