def check_sudoku(grid):
    if type(grid) is not list or len(grid) != 9:
        return None
        
    n = len(grid)    
    for row in range(n):
        if type(grid[row]) is not list or len(grid[row]) != n:
            return None
        for col in range(n):
            val = grid[row][col]
            if type(val) != int or val < 0 or val > 9:
                return False
    
    for row in range(n):
        seen = dict()
        for col in range(n):
            val = grid[row][col]
            if val != 0 and val in seen:
                return False
            seen[val] = 1
            
    for col in range(n):
        seen = dict()
        for row in range(n):
            val = grid[row][col]
            if val != 0 and val in seen:
                return False
            seen[val] = 1


    for i in range(3):
        for j in range(3):
            seen = dict()
            for ii in range(3):
                for jj in range(3):
                    row = (3*i) + ii
                    col = (3*j) + jj
                    val = grid[row][col]
                    if val != 0 and val in seen:
                        return False
                    seen[val] = 1
                    
    return True

import copy
def solve_sudoku(grid):
    res = check_sudoku(grid)
    if not res or res == None:
        return res
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                for i in range(1,10):
                    grid[row][col] = i
                    new_grid = solve_sudoku(grid)
                    if new_grid:
                        return new_grid
                return False
    return grid

    
def main():
    # solve_sudoku should return None
    ill_formed = [[5,3,4,6,7,8,9,1,2],
                  [6,7,2,1,9,5,3,4,8],
                  [1,9,8,3,4,2,5,6,7],
                  [8,5,9,7,6,1,4,2,3],
                  [4,2,6,8,5,3,7,9],  # <---
                  [7,1,3,9,2,4,8,5,6],
                  [9,6,1,5,3,7,2,8,4],
                  [2,8,7,4,1,9,6,3,5],
                  [3,4,5,2,8,6,1,7,9]]

    # solve_sudoku should return valid unchanged
    valid = [[5,3,4,6,7,8,9,1,2],
             [6,7,2,1,9,5,3,4,8],
             [1,9,8,3,4,2,5,6,7],
             [8,5,9,7,6,1,4,2,3],
             [4,2,6,8,5,3,7,9,1],
             [7,1,3,9,2,4,8,5,6],
             [9,6,1,5,3,7,2,8,4],
             [2,8,7,4,1,9,6,3,5],
             [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
    invalid = [[5,3,4,6,7,8,9,1,2],
               [6,7,2,1,9,5,3,4,8],
               [1,9,8,3,8,2,5,6,7],
               [8,5,9,7,6,1,4,2,3],
               [4,2,6,8,5,3,7,9,1],
               [7,1,3,9,2,4,8,5,6],
               [9,6,1,5,3,7,2,8,4],
               [2,8,7,4,1,9,6,3,5],
               [3,4,5,2,8,6,1,7,9]]

    # solve_sudoku should return a 
    # sudoku grid which passes a 
    # sudoku checker.
    easy = [[2,9,0,0,0,0,0,7,0],
            [3,0,6,0,0,8,4,0,0],
            [8,0,0,0,4,0,0,0,2],
            [0,2,0,0,3,1,0,0,7],
            [0,0,0,0,8,0,0,0,0],
            [1,0,0,9,5,0,0,6,0],
            [7,0,0,0,9,0,0,0,1],
            [0,0,1,2,0,0,3,0,6],
            [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
    hard = [[1,0,0,0,0,7,0,9,0],
            [0,3,0,0,2,0,0,0,8],
            [0,0,9,6,0,0,5,0,0],
            [0,0,5,3,0,0,9,0,0],
            [0,1,0,0,8,0,0,0,2],
            [6,0,0,0,0,4,0,0,0],
            [3,0,0,0,0,0,0,1,0],
            [0,4,0,0,0,0,0,0,7],
            [0,0,7,0,0,0,3,0,0]]
    
    print(check_sudoku(ill_formed)) # --> None
    print(check_sudoku(valid))     # --> True
    print(check_sudoku(invalid))   # --> False
    print(check_sudoku(easy))       # --> True
    print(check_sudoku(hard))       # --> True
    
    grid = solve_sudoku(easy)
    res = check_sudoku(grid)
    
    if not res or res == None:
        print("INVALID")
    else:
        print("Solved")
        for l in grid:
            print(l)
        
if __name__ == '__main__':
    main()
        
